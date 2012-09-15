from webtest import TestApp
import unittest

from icd10api import main

class TestICD10piApp(unittest.TestCase):

    def setUp(self):
        self.app= TestApp(main({}))

    def test_root(self):
        self.app.get('/', status=200)

    def test_apichapters(self):
        self.app.get('/api/chapters', status=200)
    def test_apichapters_query_get(self):
        self.app.get('/api/chapters', {'q':'1'}, status=307)
    def test_apichapters_query_post(self):
        self.app.post('/api/chapters', {'q':'1'}, status=307)
    def test_apichapter(self):
        self.app.get('/api/chapters/1', status=200)
    def test_apichapter_404(self):
        self.app.get('/api/chapters/not_valid', status=404)

    def test_apisections(self):
        self.app.get('/api/sections', status=200)
    def test_apisections_query_get(self):
        self.app.get('/api/sections', {'q':'a00-a09'}, status=307)
    def test_apisections_query_post(self):
        self.app.post('/api/sections', {'q':'a00-a09'}, status=307)
    def test_apisection(self):
        self.app.get('/api/sections/a00-a09', status=200)
    def test_apisection_404(self):
        self.app.get('/api/sections/not_valid', status=404)

    def test_apidiags(self):
        self.app.get('/api/diags', status=200) # TODO: time
    def test_apidiags_query_get(self):
        self.app.get('/api/diags', {'q':'a00'}, status=307)
    def test_apidiags_query_post(self):
        self.app.post('/api/diags', {'q':'a00'}, status=307)
    def test_apidiag(self):
        self.app.get('/api/diags/a00', status=200)
    def test_apidiag_404(self):
        self.app.get('/api/diags/not_valid', status=404)
