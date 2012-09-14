""" Cornice services.
"""
from cornice import Service


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

from icd10 import get_chapter, get_section, get_diag

icd10chapter = Service( name='icd10chapter',
                        path='icd10/chapter/{id}',
                        description="Get an ICD10 chapter")
@icd10chapter.get()
def get_icd10chapter(request):
    code = request.matchdict.get("id").upper()
    return get_chapter(code)


icd10section = Service( name='icd10section',
                        path='icd10/section/{id}',
                        description="Get an ICD10 section")
@icd10section.get()
def get_icd10section(request):
    code = request.matchdict.get("id").upper()
    return get_section(code)


icd10diag = Service(    name='icd10diag',
                        path='icd10/diag/{id}',
                        description="Get an ICD10 diag")
@icd10diag.get()
def get_icd10diag(request):
    code = request.matchdict.get("id").upper()
    return get_diag(code)

