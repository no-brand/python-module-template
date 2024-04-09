import unittest
from pipeline-hyphen.hello import hello_function

class HelloTest(unittest.TestCase):
    def test(self):
        result = hello_function()
        self.assertTrue(result)
