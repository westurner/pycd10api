from webtest import TestApp
import unittest

from icd10api import main

class TestICD10piApp(unittest.TestCase):

    def test_root(self):
        app = TestApp(main({}))
        app.get('/', status=200)

