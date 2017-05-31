#!/usr/bin/env python

import unittest


class TestMyThing(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_that_tests_run(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
