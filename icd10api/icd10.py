#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
walk_icd
"""

#from lxml import etree
from lxml import objectify

import os.path
DATA_PATH=os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                '../data/icd10xml')
FILE_2013=os.path.join(
            DATA_PATH,
            'ICD10CM_FY2013_Full_XML_Tabular.xml')
FILE_2011=os.path.join(
            DATA_PATH,
            'icd10cm_tabular_2011.xml')
FILE=FILE_2013

#ICD10XML_2011 = objectify.parse(open(FILE_2011))
ICD10XML_2013 = objectify.parse(open(FILE))
ICD10XML=ICD10XML_2013

NOTE_TYPES = (
    "inclusionTerm",
    "sevenChrNote",
    "includes",
    "excludes1",
    "excludes2",
    "codeFirst",
    "useAdditionalCode",
    "codeAlso",
    "notes",
    "instruction",
)

NODE_ATTRS = {
    'chapter': ['name', 'desc'],
    'section': ['id','desc'],
    'diag': ['name','desc'],
}

NODE_RECURSE = {
    'chapter': (('sections','section'),),
    'section': (('diag','diag'),),
    'diag': (('subdiag','diag'),)
}

from collections import OrderedDict
import json
class ReasonableOrderedDict(OrderedDict):
    def __str__(self):
        return json.dumps(self, indent=2)

    def __repr__(self):
        return str(self)

def node_to_dict(node, node_type='diag'):
    _node = ReasonableOrderedDict()
    for attr in NODE_ATTRS[node_type]:
        _node[attr] = unicode( getattr(node, attr, node.get(attr) ) ) # TODO

    for _type in NOTE_TYPES:
        notes =  [unicode(n) for n in node.xpath('%s/note' % _type)]
        # TODO
        if notes:
            _node[_type] = notes

    for attrname, xmlname in NODE_RECURSE[node_type]:
        tmplist = []
        for n in node.findall(xmlname):
            tmplist.append(node_to_dict(n, xmlname))
        # TODO
        if tmplist:
            _node[attrname] = tmplist

    return _node

def get_chapters():
    return [(unicode(c.name), unicode(c.desc)) for c in
        ICD10XML.xpath('//chapter')]
def get_chapter(code='1'):
    return \
        [node_to_dict(n, 'chapter') for n in
                ICD10XML.xpath("//chapter[name='%s']""" % str(code).upper() )]

def get_sections():
    return [(s.get('id'),s.text.strip())
            for s in ICD10XML.xpath('//sectionIndex/sectionRef')]
def get_section(code='A00'):
    return \
        [node_to_dict(n, 'section') for n in
                ICD10XML.xpath("//section[@id='%s']""" % code.upper() )]

def get_diags():
    return [(unicode(d.name), unicode(d.desc)) for d in
                ICD10XML.xpath('//diag')]
def get_diag(code='A00'):
    """
    walk icd path
    """
    return \
        [node_to_dict(n, 'diag') for n in
            ICD10XML.xpath("""//diag[name='%s']""" % code.upper() )]

def search(term='Cholera',
                type='diag',
                attr='desc',
                caseinsensitive=False):
    NS = {'re':'http://exslt.org/regular-expressions'}
    return \
        [node_to_dict(n, type) for n in
            ICD10XML.xpath(
            '''//%s[re:test(%s, '%s', '%s')]''' % (
                type, attr, term,
                caseinsensitive and 'i' or ''),
            namespaces=NS)]

def lookup(code):
    code = code.upper()
    diag = get_diag(code)
    if diag:
        ret = diag[0]['name'], diag[0]['desc']
    else:
        if '.' in code:
            parentcode = code.split('.',1)[0]
            ret = code, '-->', lookup(parentcode)
        else:
            sect = get_section(code)
            if sect:
                ret = sect[0].get('name')
                if diag:
                    ret = ret, diag[0].get('desc')
            else:
                ret = code, '??'
    return ret

import unittest
class Test_walk_icd(unittest.TestCase):
    def test_get_diag(self):
        CODES = ['A00']
        for c in CODES:
            print( get_diag(c) )

    #def test_lookup_codes(self):
    #    import pickle
    #    codes = pickle.load(file('../../../data/codes.pickle'))
    #    for c in codes:
    #        print( lookup(c) )

import sys
class Test_main(unittest.TestCase):
    def setUp(self):
        sys.args = ['./icd10.py']

    def test_chapter(self):
        sys.args.extend(['--chapter', 1])
        main()

    def test_section(self):
        sys.args.extend(['--section', 'A00-A09'])
        main()

    def test_diag(self):
        sys.args.extend(['--diag', 'B96.81'])
        main()

    def test_search(self):
        sys.args.extend(['--search', 'pylori'])
        main()

    def test_lookup(self):
        sys.args.append('B96.81')
        main()

def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    # default: lookup(a) for a in args

    prs.add_option('-s', '--search',
                    dest='search',
                    help='Search diagnoses for a given term')

    prs.add_option('--chapter',
                    dest='chapter',
                    help='Lookup a chapter')
    prs.add_option('--section',
                    dest='section',
                    help='Lookup a section')
    prs.add_option('--diag',
                    dest='diag',
                    help='Lookup a diag')

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())
    elif opts.search:
        for s in search(opts.search):
            print( s )
    elif opts.chapter:
        for c in get_chapter(opts.chapter):
            print( c )
    elif opts.section:
        for s in get_section(opts.section):
            print( s )
    elif opts.diag:
        for d in get_diag(opts.diag):
            print( d )
    else:
        for c in args:
            print( lookup(c) )

if __name__ == "__main__":
    main()
