#!/usr/bin/env python
"""
Description

 Test head_http.py script

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
#import head_http

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "head_http.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestHeadHttp(unittest.TestCase):
    """ Unit tests for head_http.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {}".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run("python3 {}".format(script_path))
        self.assertEqual(status, 0)

    def test_google(self):
        out, status = cmd.run("python {} http://google.ca".format(script_path))
        self.assertEqual(status, 0)

        # Date: Wed, ...
        self.assertTrue(len(str(out)) > 0)
        self.assertTrue(str(out).find("Date:") != -1)

    def test_bad_url(self):
        out, status = cmd.run(
            "python {}  http://hgoogle.hca".format(script_path))
        self.assertEqual(status, -1)

if __name__ == "__main__":
    unittest.main()
    exit(0)
