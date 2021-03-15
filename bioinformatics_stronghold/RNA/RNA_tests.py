from RNA import GenerateRNA
from unittest import TestCase

class RNATest(TestCase):
    def test_rna(self):
        string = 'GATGGAACTTGACTACGTAAATT'
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU', GenerateRNA(string))
