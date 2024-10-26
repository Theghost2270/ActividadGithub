import logging
import time
import unittest

logging.basicConfig(filename="emp.log", level= logging.INFO,format='%(levelname)s:%(message)s', filemode='w')
logger = logging.getLogger()


begin = time.time()

print(f" Strating time of the program {begin}")

class Testarithmetic(unittest.TestCase):

    def test_addition(self):
        val1 = 10
        val2 = 8
        final_value = val1 + val2
        self.assertEqual(final_value, 18)
        logger.info("the addition of values are here")

    def test_subtraction(self):
        val3 = 60
        val4 = 20
        final_value = val3 - val4
        self.assertTrue(final_value, 40)
        logger.warning("val 3 should be greater then val4")
        logger.error("something is wrong here")

    def test_divide(self):
        val5 = 12
        val6 = 6
        val7 = 2

        final_value = val5/val6
        final_value1 = val6/val7
        self.assertGreater(final_value1,final_value)
        logger.exception("values divided successfully.")



end = time.time()
print(f"program ending at {end}")
print(f" total time taken by program {end - begin}")

if __name__ == '_main_':
    unittest.main()
