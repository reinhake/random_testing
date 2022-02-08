import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0,1000):
            val = random.randint(1000000000000000, 9999999999999999)
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
