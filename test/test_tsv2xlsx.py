#!/usr/bin/env python
"""
Description

 Test tsv2xlsx.py script

Note
 - works with python 2.7 and 3.6

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
#import tsv2xlsx

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "tsv2xlsx.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestTsv2Xlsx(unittest.TestCase):
    """ Unit tests for tsv2xlsx.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -v".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run(
            "python3 {} -v".format(os.path.join(script_path, script_path)))
        self.assertEqual(status, 0)

    def test_xlsx(self):
        """ test creation of excel file """
        data_path = os.path.join(os.path.abspath(""), "test/data/table.txt")
        out, status = cmd.run(
            "python {} -f {} -x table.xlsx".format(script_path, data_path))
        self.assertEqual(status, 0)

        statinfo = os.stat("table.xlsx")
        self.assertTrue(statinfo.st_size != 0)
        os.remove("table.xlsx")

if __name__ == "__main__":
    unittest.main()
    exit(0)
