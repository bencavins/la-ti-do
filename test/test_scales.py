import unittest

from music import scales


class TestScale(unittest.TestCase):

    def test_tonic(self):
        c_major = scales.Scale(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        self.assertEqual(c_major.tonic, 'C')
