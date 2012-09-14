from webtest import TestApp
import unittest

from icd10api import main

class TestICD10piApp(unittest.TestCase):

    def test_root(self):
        app = TestApp(main({}))
        app.get('/', status=200)

    def test_icd10chapter(self):
        app = TestApp(main({}))
        app.get('/icd10/chapter/1', status=200)

    def test_icd10section(self):
        app = TestApp(main({}))
        app.get('/icd10/section/a00-a09', status=200)

    def test_icd10diag(self):
        app = TestApp(main({}))
        app.get('/icd10/diag/a00', status=200)
