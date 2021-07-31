#!/usr/bin/env python
"""
Description

 Test ping.py script

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
#import ping

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "ping.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestPing(unittest.TestCase):
    """ Unit tests for ping.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} ".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run("python3 {} ".format(script_path))
        self.assertEqual(status, 0)

    @unittest.skip("require sudo")
    def test_google(self):
        out, status = cmd.run(
            "python2 {} http://google.ca ".format(script_path))
        self.assertEqual(status, 0)

    def test_bad_url(self):
        out, status = cmd.run(
            "python2 {} hhttp://hgoogle.hca ".format(script_path))
        self.assertEqual(status, -1)

if __name__ == "__main__":
    unittest.main()
    exit(0)
