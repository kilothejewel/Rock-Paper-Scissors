import unittest #testing framework
from test_base import captured_io, captured_output
from io import StringIO
from main import *
from main import readfile, find_me_some_hoes

class TestMain(unittest.TestCase):

    def test_readfile(self):
        expected = readfile()
        actual = ["Move 10 metres forward"]

        self.assertIsNotNone(actual) #Makes sure our test file doesnt return a none.
        self.assertEqual(len(actual),4)
        self.assertTrue("Move" in actual)
        self.assertTrue("Turn" in actual)

    def test_index1IsDigit(self):
        actual = readfile()
        expected = ["Move 10 meters forward"]
        index = self.getIndex(actual,1)
        self.assertEqual(index,10)

    def test_terminal(self):
        with captured_io(StringIO("test\n")) as (out):
            output = getStep("Move, 10,")
if __name__=="_main_":
    unittest.main()