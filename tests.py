import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0,100000):
            val = "4" + str(random.randint(10000000000000, 999999999999999))
            credit_card_validator(val)

    def test2(self):
        for i in range(0,100000):
            val = "5" + str(random.randint(10000000000000, 999999999999999))
            credit_card_validator(val)

    def test3(self):
        for i in range(0,50000):
            val = "22" + str(random.randint(10000000000000, 999999999999999))
            credit_card_validator(val)

    def test4(self):
        for i in range(0,50000):
            val = "27" + str(random.randint(10000000000000, 30000000000000))
            credit_card_validator(val)

    def test5(self):
        for i in range(0,100000):
            val = "3" + str(random.randint(30000000000000, 800000000000000))
            credit_card_validator(val)

    def test6(self):
        for i in range(0,1000000):
            val = random.randint(10000000000000, 99999999999999999)
            credit_card_validator(val)


# 4528343118254528 bad checksum test 4
# 7115125492487115 bad checksum test 4
# 4721512696974721 bad checksum test 4
# 5294487807775294 good checksum
# 1212034808503677 good checksum

# 4590829111103396 good checksum test 5
# 4661311112413367 good checksum test 5
# 4934511720111151 good
# 5401811114907425 good
# 5493811112410124 good

# 342695942809769 good checksum and length test 3
if __name__ == '__main__':
    unittest.main()
