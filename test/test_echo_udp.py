#!/usr/bin/env python
"""
Description

 Test echo_udp.py script

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
#import echo_udp

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "echo_udp.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestEchoUDP(unittest.TestCase):
    """ Unit tests for echo_udp.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -v".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run("python3 {} -v".format(script_path))
        self.assertEqual(status, 0)


if __name__ == "__main__":
    unittest.main()
    exit(0)
