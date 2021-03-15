from DNA import nucleotides_count
from unittest import TestCase

class DNATest(TestCase):
    
    def test_nucl_count(self):
        string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        self.assertEqual('20 12 17 21', nucleotides_count(string))
