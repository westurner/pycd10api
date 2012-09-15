""" icd10api resources
"""
from cornice import Service
from cornice.resource import resource, view


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

import icd10

@resource(collection_path='/api/chapters', path='/api/chapters/{id}')
class Chapter(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        return {'chapters': icd10.get_chapters() } # TODO

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        return icd10.get_chapter(code)


@resource(collection_path='/api/sections', path='/api/sections/{id}')
class Section(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        return {'sections': icd10.get_sections() } # TODO

    def collection_post(self):
        # TODO: redirect to self.get
        return None

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        return icd10.get_section(code)


@resource(collection_path='/api/diags', path='/api/diags/{id}')
class Diag(object):
    def __init__(self, request):
        self.request = request

    @view(renderer='json')
    def collection_get(self):
        return {'diags': icd10.get_diags() } # TODO: memoize?

    def collection_post(self):
        #TODO: redirect to self.get
        return None

    @view(renderer='json')
    def get(self):
        code = self.request.matchdict.get("id").upper()
        return icd10.get_diag(code)

