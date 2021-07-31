#!/usr/bin/env python
"""
Description

 Test cmd module

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

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script_path = os.path.abspath("../")


class TestLibCmd(unittest.TestCase):
    """ Test lib/cmd """

    @unittest.skipIf(sys.platform.startswith("win"), "fail on windows")
    def test_cd(self):
        ok = cmd.can_run("cd .")
        self.assertTrue(ok)

    @unittest.skipIf(sys.platform.startswith("win"), "fail on windows")
    def test_echo(self):
        out, ok = cmd.run("echo echo...")
        _os = sys.platform
        print("{} echo: {}".format(_os, str(out)))
        self.assertEqual(ok, 0)

    def test_impossible(self):
        ok = cmd.can_run("__impossible_cmd_ -V")
        self.assertFalse(ok)

    def test_python(self):
        out, status = cmd.run("python -V")
        print("python -V: {}".format(str(out)))
        self.assertEqual(status, 0)

    def test_python2(self):
        out, status = cmd.run("python2 -V")
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run("python3 -V")
        self.assertEqual(status, 0)

if __name__ == "__main__":
    unittest.main()
    exit(0)
