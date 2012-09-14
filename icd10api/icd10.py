#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
walk_icd
"""

#from lxml import etree
from lxml import objectify

FILE_2013='ICD10CM_FY2013_Full_XML_Tabular.xml'
FILE_2011='icd10cm_tabular_2011.xml'
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

def get_chapter(code='1'):
    return \
        [node_to_dict(n, 'chapter') for n in
                ICD10XML.xpath("//chapter[name='%s']""" % str(code).upper() )]

def get_section(code='A00'):
    return \
        [node_to_dict(n, 'section') for n in
                ICD10XML.xpath("//section[@id='%s']""" % code.upper() )]

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
                ret = sect[0]['name'], diag[0]['desc']
            else:
                ret = code, '??'
    return ret

import unittest
class Test_walk_icd(unittest.TestCase):
    def test_get_diag(self):
        CODES = ['A00']
        for c in CODES:
            print( get_diag(c) )

    def test_lookup_codes(self):
        import pickle
        codes = pickle.load(file('../../../data/codes.pickle'))
        for c in codes:
            print( lookup(c) )

def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

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

    import json
    print( json.dumps(get_section('A00-A09'),indent=2) )

if __name__ == "__main__":
    main()
