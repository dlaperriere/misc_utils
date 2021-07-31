#!/usr/bin/env python
"""
Description

 Test parallel_cmd.py script

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
#import parallel_cmd

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script = "parallel_cmd.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestParallelCmd(unittest.TestCase):
    """ Unit tests for parallel_cmd.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -v".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run(
            "python3 {} -v".format(os.path.join(script_path, script_path)))
        self.assertEqual(status, 0)

    @unittest.skipIf(sys.platform.startswith("win"), "requires ls, gzip and gunzip")
    def test_gzip(self):
        """ test gzip/gunzip on a text file """
        data_path = os.path.join(os.path.abspath(""), "test/data/table.txt")
        gzdata_path = os.path.join(
            os.path.abspath(""), "test/data/table.txt.gz")

        out, status = cmd.run(
            "ls {} | python {} -f - -c \"{}\"".format(data_path, script_path, "gzip -v"))
        self.assertEqual(status, 0)
        self.assertTrue(os.path.isfile(gzdata_path))

        out, status = cmd.run(
            "ls {} | python {} -f - -c \"{}\"".format(gzdata_path, script_path, "gunzip -v"))
        self.assertEqual(status, 0)
        self.assertTrue(os.path.isfile(data_path))


if __name__ == "__main__":
    unittest.main()
    exit(0)
