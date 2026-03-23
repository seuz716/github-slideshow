#!/usr/bin/env python3
"""
Run all tests for the Jekyll/Reveal.js presentation project.

Usage:
    python run_tests.py
    python run_tests.py -v  # verbose mode
"""

import unittest
import sys
from pathlib import Path

# Add the tests directory to the path
tests_dir = Path(__file__).parent
sys.path.insert(0, str(tests_dir))

if __name__ == '__main__':
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=tests_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2 if '-v' in sys.argv else 1)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
