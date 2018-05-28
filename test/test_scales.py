import unittest

from music import scales


class TestScale(unittest.TestCase):

    def test_tonic(self):
        c_major = scales.Scale(['C', 'D', 'E', 'F', 'G', 'A', 'B'])

        self.assertEqual(c_major.tonic, 'C')

    def test_degree(self):
        c_major = scales.Scale(['C', 'D', 'E', 'F', 'G', 'A', 'B'])

        self.assertEqual(c_major.degree(1), 'C')
        self.assertEqual(c_major.degree(2), 'D')
        self.assertEqual(c_major.degree(3), 'E')
        self.assertEqual(c_major.degree(4), 'F')
        self.assertEqual(c_major.degree(5), 'G')
        self.assertEqual(c_major.degree(6), 'A')
        self.assertEqual(c_major.degree(7), 'B')
