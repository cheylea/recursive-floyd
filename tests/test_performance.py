# Performance Tests for Floyd Warshall Function

# Update path
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall function
from floydwarshall.function import floydWarshall

# Import Floyd Warshall test cases
from test_cases import (sample_a, sample_b, sample_c, sample_d)

# Import testing package
import cProfile

# Performance Tests
cProfile.run("floydWarshall(sample_a)")

cProfile.run("floydWarshall(sample_b)")

cProfile.run("floydWarshall(sample_c)")

cProfile.run("floydWarshall(sample_d)")
