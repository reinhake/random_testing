import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    # testing visa prefix
    def test1(self):
        for i in range(0,100000):
            val = "4" + str(random.randint(10000000000000, 999999999999999))
            credit_card_validator(val)

    # bug two seems to involve a visa prefix followed by a 0
    def test2(self):
        for i in range(0,100000):
            val = "40" + str(random.randint(10000000000000, 99999999999999))
            credit_card_validator(val)

    # testing first set of mastercard prefixes  
    def test3(self):
        for i in range(0,100000):
            val = "5" + str(random.randint(10000000000000, 999999999999999))
            credit_card_validator(val)

    # testing second set lowerbounds of mastercard prefixes
    def test4(self):
        for i in range(0,50000):
            val = "22" + str(random.randint(10000000000000, 99999999999999))
            credit_card_validator(val)

    # testing second set upperbounds of mastercard prefixes
    def test5(self):
        for i in range(0,50000):
            val = "27" + str(random.randint(10000000000000, 30000000000000))
            credit_card_validator(val)

    # testing AmEx prefixes
    def test6(self):
        for i in range(0,100000):
            val = "3" + str(random.randint(30000000000000, 800000000000000))
            credit_card_validator(val)

    # no specific prefixes just testing any length 14 to 17
    def test7(self):
        for i in range(0,100000):
            val = random.randint(10000000000000, 99999999999999999)
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
