import unittest
from main import validate_sequence, translate_sequence


class TestCodonTableGenerator(unittest.TestCase):

    def test_valid_dna(self):
        self.assertTrue(validate_sequence("ATGGCT"))

    def test_valid_rna(self):
        self.assertTrue(validate_sequence("AUGGCU"))

    def test_invalid_sequence(self):
        self.assertFalse(validate_sequence("ATGX123"))

    def test_mixed_dna_rna(self):
        self.assertFalse(validate_sequence("ATGUGC"))

    def test_empty_sequence(self):
        self.assertFalse(validate_sequence(""))

    def test_incomplete_codon(self):
        codons, amino_acids, incomplete = translate_sequence("ATGGCTA")
        self.assertEqual(incomplete, "A")

    def test_correct_translation(self):
        codons, amino_acids, incomplete = translate_sequence("ATGGCT")
        self.assertEqual(amino_acids, ["Methionine", "Alanine"])

    def test_codon_table_contains_64_codons(self):
        from main import codon_table
        self.assertEqual(len(codon_table), 64)

    def test_stop_codon_translation(self):
        codons, amino_acids, incomplete = translate_sequence("TAA")
        self.assertEqual(amino_acids, ["Stop"])

    def test_rna_translation(self):
        codons, amino_acids, incomplete = translate_sequence("AUGGCU")
        self.assertEqual(amino_acids, ["Methionine", "Alanine"])

if __name__ == "__main__":
    unittest.main()
