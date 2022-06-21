#Unit Testing
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Hopper"
        expected = "Hopper"
        self.assertEqual(rearrange_name(testcase), expected)    

unittest.main()

# Best of Unit Testing Standard Library Module

# Understand a Basic Example:

# https://docs.python.org/3/library/unittest.html#basic-example
# Understand how to run the tests using the Command Line:

# https://docs.python.org/3/library/unittest.html#command-line-interface
# Understand various Unit Test Design Patterns:

# https://docs.python.org/3/library/unittest.html#organizing-test-code
# Understand the uses of setUp, tearDown; setUpModule and tearDownModule

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

# assertEqual(a, b)
# a == b
# assertNotEqual(a, b)
# a != b
# assertTrue(x)
# bool(x) is True
# assertFalse(x)
# bool(x) is False
# assertIs(a, b)
# a is b

# assertIsNot(a, b)
# a is not b

# assertIsNone(x)

# assertIsNotNone(x)
# x is not None
# 3.1
# assertIn(a, b)
# a in b
# 3.1
# assertNotIn(a, b)
# a not in b

# assertIsInstance(a, b)
# isinstance(a, b)

# assertNotIsInstance(a, b)
# not isinstance(a, b)

