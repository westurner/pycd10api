""" icd10api resources
"""
from cornice import Service
from cornice.resource import resource, view
from pyramid.httpexceptions import HTTPNotFound, HTTPTemporaryRedirect

hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

import icd10

@resource(collection_path='/api/chapters', path='/api/chapters/{id}',
         description="ICD10 Chapters")
class Chapter(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'chapters': icd10.get_chapters() }

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/chapters/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        chapter = icd10.get_chapter(code)
        if not chapter:
            raise HTTPNotFound()
        return chapter


@resource(collection_path='/api/sections', path='/api/sections/{id}',
            description="ICD10 Sections")
class Section(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'sections': icd10.get_sections() }

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/sections/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        sections = icd10.get_section(code)
        if not sections:
            raise HTTPNotFound()
        return sections


@resource(collection_path='/api/diags', path='/api/diags/{id}',
            description="ICD10 Diags")
class Diag(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        if 'q' in self.request.params:
            return self.collection_post()
        return {'diags': icd10.get_diags() } # TODO: memoize?

    def collection_post(self):
        return HTTPTemporaryRedirect(
                '/api/diags/%s' % self.request.params.get('q'))

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        diags = icd10.get_diag(code)
        if not diags:
            raise HTTPNotFound()
        return diags

