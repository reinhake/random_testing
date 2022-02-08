import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0,3000):
            val = random.randint(10000000000000, 99999999999999999)
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
