import unittest

from manspy.cli import do_cmd


class TestCLI(unittest.TestCase):
    def test_cli(self):
        do_cmd([])
        self.assertEqual(True, False)


