#!/usr/bin/env python
"""
Description

 Test md5 module

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

from lib import cmd, md5

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

script_path = os.path.abspath(os.path.join(".", "lib", "md5.py"))


class TestLibMd5(unittest.TestCase):
    """ Test lib/md5 """

    def test_md5_str_md5(self):
        """test md5 1bc29b36f623ba82aaf6724fd3b16718 """
        self.assertTrue(md5.md5sum("md5"), "1bc29b36f623ba82aaf6724fd3b16718")

    def test_md5_wiki_example(self):
        """test wikipedia example  
           The quick brown fox jumps over the lazy dog
           9e107d9d372bb6826bd81d3542a419d6 
         """
        self.assertEqual(md5.md5sum(
            "The quick brown fox jumps over the lazy dog"), "9e107d9d372bb6826bd81d3542a419d6")

    def test_python(self):
        """ run lib/md5.py script with default python """
        out, status = cmd.run("python {} {}".format(script_path, "md5 python"))
        self.assertEqual(status, 0)

    def test_python2(self):
        """ run lib/md5.py script with python2 """
        out, status = cmd.run(
            "python2 {} {}".format(script_path, "md5 python2"))
        self.assertEqual(status, 0)

    def test_python3(self):
        """ run lib/md5.py script with python3 """
        out, status = cmd.run(
            "python3 {} {}".format(script_path, "md5 python3"))
        self.assertEqual(status, 0)

    def test_utf8_python2_3(self):
        """ run lib/md5.py with python2 and 3 with utf8 file """
        utf8_path = os.path.abspath(
            os.path.join(".", "test", "data", "utf8.txt"))
        md5_v2, status2 = cmd.run(
            "python2 {} {}".format(script_path, utf8_path))
        self.assertEqual(status2, 0)

        md5_v3, status3 = cmd.run(
            "python3 {} {}".format(script_path, utf8_path))
        self.assertEqual(status3, 0)
        self.assertTrue(str(md5_v2).find(
            "a28d7d1d9be5aff95d356e8b52b0244e") != -1)
        self.assertTrue(str(md5_v3).find(
            "a28d7d1d9be5aff95d356e8b52b0244e") != -1)
        self.assertEqual(md5_v2, md5_v3)


if __name__ == "__main__":
    unittest.main()
    exit(0)
