import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0,10000):
            val = "4" + str(random.randint(100000000000000, 999999999999999))
            credit_card_validator(val)

    def test2(self):
        for i in range(0,10000):
            val = "5" + str(random.randint(100000000000000, 999999999999999))
            credit_card_validator(val)

    def test3(self):
        for i in range(0,10000):
            val = "2" + str(random.randint(200000000000000, 8000000000000000))
            credit_card_validator(val)

    def test4(self):
        for i in range(0,10000):
            val = "3" + str(random.randint(30000000000000, 800000000000000))
            credit_card_validator(val)

    def test5(self):
        for i in range(0,1000000):
            val = random.randint(1000000000, 99999999999999999999)
            credit_card_validator(val)
# 4528343118254528 bad checksum test 4
# 7115125492487115 bad checksum test 4
# 4721512696974721 bad checksum test 4

# 4590829111103396 good checksum test 5
# 4661311112413367 good checksum test 5

# 342695942809769 good checksum and length test 3
if __name__ == '__main__':
    unittest.main()
