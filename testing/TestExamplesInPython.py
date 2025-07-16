import unittest
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some1'
        logging.debug("A DEBUG Message"+a)
        logging.info("\n")
        logging.info("An INFO"+b)
        self.assertEqual(a, b)
        # logging.warning("A WARNING")
        # logging.error("An ERROR")
        # logging.critical("A message of CRITICAL severity")

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
