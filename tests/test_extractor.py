import unittest
from doi_extractor import DOIExtractor

class TestDOIExtractor(unittest.TestCase):
    def test_extract_dois_from_bibtex(self):
        extractor = DOIExtractor('tests/sample.bib')
        extractor.extract()
        self.assertIn('10.1234/example', extractor.dois)

    def test_extract_dois_from_ris(self):
        extractor = DOIExtractor('tests/sample.ris')
        extractor.extract()
        self.assertIn('10.1234/example', extractor.dois)

    def test_extract_dois_from_bibtex_multiple(self):
        extractor = DOIExtractor('tests/sample_multi.bib')
        extractor.extract()
        self.assertIn('10.1234/example1', extractor.dois)
        self.assertIn('10.1234/example2', extractor.dois)

    def test_extract_dois_from_ris_multiple(self):
        extractor = DOIExtractor('tests/sample_multi.ris')
        extractor.extract()
        self.assertIn('10.1234/example1', extractor.dois)
        self.assertIn('10.1234/example2', extractor.dois)

    def test_extract_dois_from_bibtex_no_doi(self):
        extractor = DOIExtractor('tests/sample_no_doi.bib')
        extractor.extract()
        self.assertEqual(len(extractor.dois), 0)

    def test_extract_dois_from_ris_no_doi(self):
        extractor = DOIExtractor('tests/sample_no_doi.ris')
        extractor.extract()
        self.assertEqual(len(extractor.dois), 0)

if __name__ == '__main__':
    unittest.main()
