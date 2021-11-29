# Unit Tests for the Flord Warshall function

# Update path
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall function
from floydwarshall.function import floydWarshall

# Import Floyd Warshall test cases
from test_cases import (sample_a, sample_b, sample_c, sample_d,
                        output_a, output_b, output_c, output_d)

# Import testing package
import unittest

# Unit Tests
class TestFloyd(unittest.TestCase):

    def test_floyd_a(self):
        self.assertEqual(floydWarshall(sample_a), output_a, "Output incorrect")

    def test_floyd_b(self):
        self.assertEqual(floydWarshall(sample_b), output_b, "Output incorrect")

    def test_floyd_c(self):
        self.assertEqual(floydWarshall(sample_c), output_c, "Output incorrect")

    def test_floyd_d(self):
        self.assertEqual(floydWarshall(sample_d), output_d, "Output incorrect")

if __name__ == '__main__':
    unittest.main()
