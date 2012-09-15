from webtest import TestApp
import unittest

from icd10api import main

class TestICD10piApp(unittest.TestCase):

    def test_root(self):
        app = TestApp(main({}))
        app.get('/', status=200)

    def test_apichapters(self):
        app = TestApp(main({}))
        app.get('/api/chapters', status=200)
    def test_apichapter(self):
        app = TestApp(main({}))
        app.get('/api/chapters/1', status=200)

    def test_apisections(self):
        app = TestApp(main({}))
        app.get('/api/sections', status=200)
    def test_apisection(self):
        app = TestApp(main({}))
        app.get('/api/sections/a00-a09', status=200)

    def test_apidiags(self):
        app=TestApp(main({}))
        app.get('/api/diags', status=200) # TODO: time
    def test_apidiag(self):
        app = TestApp(main({}))
        app.get('/api/diags/a00', status=200)
