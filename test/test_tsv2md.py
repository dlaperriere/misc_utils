#!/usr/bin/env python
"""
Description

 Test tsv2md.py script

Note
 - works with python 2.7 and 3.5

Author
  David Laperriere <dlaperriere@outlook.com>

"""

from __future__ import print_function

import os
import sys
import unittest

sys.path.append(os.path.abspath(""))
sys.path.append(os.path.abspath("../"))

from lib import cmd
#import tsv2md

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "tsv2md.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestTsv2MD(unittest.TestCase):
    """ Unit tests for tsv2md.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -v".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run(
            "python3 {} -v".format(os.path.join(script_path, script_path)))
        self.assertEqual(status, 0)

    def test_markdown(self):
        """ test column separator in markdown output """
        data_path = os.path.join(os.path.abspath(""), "test/data/table.txt")
        out, status = cmd.run("python {} -f {}".format(script_path, data_path))
        self.assertEqual(status, 0)
        self.assertTrue(str(out).find(
            "--------- | ----------- | -----------") != -1)

        tout, tstatus = cmd.run(
            "python {} -t -f {}".format(script_path, data_path))
        self.assertEqual(tstatus, 0)
        self.assertTrue(str(tout).find("----------- | -----------") != -1)

        self.assertTrue(str(tout) != str(out))

if __name__ == "__main__":
    unittest.main()
    exit(0)
