import unittest
from pipeline.hello import hello_function

class HelloTest(unittest.TestCase):
    def test(self):
        result = hello_function()
        self.assertTrue(result)
