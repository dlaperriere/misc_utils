#!/usr/bin/env python
"""
Description

 Test transpose.py script

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
#import transpose

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "transpose.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestTranspose(unittest.TestCase):
    """ Unit tests for transpose.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {}".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run("python3 {}".format(script_path))
        self.assertEqual(status, 0)

    def test_transpose(self):
        """ test replacement of blank by NA """
        data_path = os.path.join(os.path.abspath(""), "test/data/table.txt")
        out, status = cmd.run("python {} {}".format(script_path, data_path))
        self.assertEqual(status, 0)
        self.assertTrue(str(out).find("NA") != -1)


if __name__ == "__main__":
    unittest.main()
    exit(0)
