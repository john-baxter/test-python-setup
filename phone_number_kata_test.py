import unittest
from phone_number_kata import create_phone_number

class TestTest(unittest.TestCase):
  def test_setup(self):
    pass

class CreatePhoneNumberTest(unittest.TestCase):
  def test_input_is_all_zeroes(self):
    n = [0,0,0,0,0,0,0,0,0,0]
    expected_result = "(000) 000-0000"
    actual_result = create_phone_number(n)

    self.assertEqual(actual_result, expected_result)
  

if __name__ == '__main__':
  unittest.main(verbosity = 2)