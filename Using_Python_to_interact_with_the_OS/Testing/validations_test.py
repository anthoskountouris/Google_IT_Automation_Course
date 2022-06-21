import unittest

from Raising_Errors import validateUser

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validateUser("validuser", 3), True)
        
    def test_too_short(self):
        self.assertEqual(validateUser("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validateUser("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validateUser,"user", -1)

# Run the tests
unittest.main()