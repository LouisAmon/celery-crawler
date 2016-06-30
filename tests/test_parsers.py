# coding: utf-8
import unittest

class TestMyParser(unittest.TestCase):

    def setUp(self):
        self.parser = MyParser()
        fixture_path = 'tests/fixtures/sample.html'
        with open(fixture_path, 'r') as f:
            self.markup = f.read()

    def test_processing(self):
        data = self.parser.process(markup=self.markup)
        # Check that every value exists and is not empty
        for k,v in data:
            self.assertTrue(v)
