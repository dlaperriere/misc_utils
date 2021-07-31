#!/usr/bin/env python
"""
Description

 Test convert_eol.py script

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

from lib import cmd, md5
#import convert_eol

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"


script = "convert_eol.py"
script_path = os.path.join(os.path.abspath(""), script)


class TestConvertEOL(unittest.TestCase):
    """ Unit tests for convert_eol.py  """

    def test_python2(self):
        out, status = cmd.run("python2 {} -v".format(script_path))
        self.assertEqual(status, 0)

    def test_python3(self):
        out, status = cmd.run(
            "python3 {} -v".format(os.path.join(script_path, script_path)))
        self.assertEqual(status, 0)

    def test_dos2unix(self):
        """ test dos 2 unix conversion """
        dos_data_path = os.path.join(os.path.abspath(""), "test/data/t.dos")
        dos_md5 = md5.md5sum(dos_data_path)
        unix_data_path = os.path.join(
            os.path.abspath(""), "test/data/t.unix")
        unix_md5 = md5.md5sum(unix_data_path)

        # dos -> unix
        out, status = cmd.run(
            "python {} {} {}".format(script_path, "dos2unix", dos_data_path))
        self.assertEqual(status, 0)
        newmd5 = md5.md5sum(dos_data_path)
        self.assertTrue(newmd5 != dos_md5)
        self.assertTrue(newmd5 == unix_md5)

        # unix -> dos
        out, status = cmd.run(
            "python {} {} {}".format(script_path, "unix2dos", dos_data_path))
        self.assertEqual(status, 0)
        newmd5 = md5.md5sum(dos_data_path)
        self.assertTrue(newmd5 == dos_md5)
        self.assertTrue(newmd5 != unix_md5)

    def test_mac2unix(self):
        """ test mac 2 unix conversion """
        mac_data_path = os.path.join(os.path.abspath(""), "test/data/t.mac")
        mac_md5 = md5.md5sum(mac_data_path)
        unix_data_path = os.path.join(
            os.path.abspath(""), "test/data/t.unix")
        unix_md5 = md5.md5sum(unix_data_path)

        # mac -> unix
        out, status = cmd.run(
            "python {} {} {}".format(script_path, "mac2unix", mac_data_path))
        self.assertEqual(status, 0)
        newmd5 = md5.md5sum(mac_data_path)
        self.assertTrue(newmd5 != mac_md5)
        self.assertTrue(newmd5 == unix_md5)

        # unix -> mac
        out, status = cmd.run(
            "python {} {} {}".format(script_path, "unix2mac", mac_data_path))
        self.assertEqual(status, 0)
        newmd5 = md5.md5sum(mac_data_path)
        self.assertTrue(newmd5 == mac_md5)
        self.assertTrue(newmd5 != unix_md5)

if __name__ == "__main__":
    unittest.main()
    exit(0)
