''' pycd10api resource and index views
'''
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPTemporaryRedirect
from cornice.resource import resource, view

@view_config(route_name='index')
def index(request):
    '''Return the index page'''
    return Response('<html><head><title>ICD10API Index</title></head></html>')

import icd.cm as icd10cm

@resource(collection_path='/api/cm/chapters', path='/api/cm/chapters/{id}',
         description='ICD10 CM Chapters')
class Chapter(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'chapters': icd10cm.get_chapters() }

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/cm/chapters/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get('id').upper()
        chapter = icd10cm.get_chapter(code)
        if not chapter:
            raise HTTPNotFound()
        return chapter


@resource(collection_path='/api/cm/sections', path='/api/cm/sections/{id}',
            description='ICD10 CM Sections')
class Section(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'sections': icd10cm.get_sections() }

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/cm/sections/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get('id').upper()
        sections = icd10cm.get_section(code)
        if not sections:
            raise HTTPNotFound()
        return sections


@resource(collection_path='/api/cm/diags', path='/api/cm/diags/{id}',
            description='ICD10 CM Diags')
class Diag(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'diags': icd10cm.get_diags() } # TODO: memoize?

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/cm/diags/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get('id').upper()
        diags = icd10cm.get_diag(code)
        if not diags:
            raise HTTPNotFound()
        return diags

