import unittest
form models.base import base

class TestBase(unittest.testcase):
    def test_init_with_id(self):
        b1 = Base(id=2)
        b2 = Base(id=0)
        self.assertEqual(b1, 2)
        self.assertEqual(b2, 0)
    def test_init_without_id(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3, 1)
        self.assertEqual(b4, 2)
    def test_init_negative_id(self):
        b5 = Base(id=-4)
        self.assertEqual(b5, -4)
if __name__ == "__main__":
    unittest.main()
