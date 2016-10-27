#!/usr/bin/env python
"""
Description

 Test doc2md.py script

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

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "doc2md.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestDoc2MD(unittest.TestCase):
    """ Unit tests for doc2md.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -h".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run(
            "python3 {} -h".format(os.path.join(script_path, script_path)))
        self.assertEqual(status, 0)


if __name__ == "__main__":
    unittest.main()
    exit(0)
