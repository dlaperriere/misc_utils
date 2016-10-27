"""
Generate MD5 hash of a file or string
"""

from __future__ import print_function

import hashlib
import os
import sys

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

__all__ = ['md5sum']

# Python version compat
if sys.version_info[0] <= 2:
    Py3 = False
elif sys.version_info[0] >= 3:
    Py3 = True


def usage():
    """ Show script parameters """
    print("Usage: md5.py file|string")
    sys.exit(0)


def read_file(filename):
    """read file without converting line endings"""
    if Py3:
        return open(filename, "r", newline='')
    return open(filename, "rb")

# md5


def string_md5(string):
    """ generate md5 hash of a string """
    if Py3:
        return hashlib.md5(string.encode('utf-8')).hexdigest()
    return hashlib.md5(string.decode('utf8', 'ignore').encode('utf-8')).hexdigest()


def file_md5(filename):
    """ generate md5 hash of a file """
    file_o = read_file(filename)
    file_str = file_o.read()
    file_o.close()
    return string_md5(file_str)


def md5sum(str_or_file):
    """ generate md5 hash of a file or string """
    md5_hash = "?"
    if os.path.isfile(str_or_file):
        md5_hash = file_md5(str_or_file)
    else:
        md5_hash = string_md5(str_or_file)
    return md5_hash

# MAIN


def main():
    """ Main: check parameters and generate md5 hash """

    # check parameters
    if len(sys.argv) >= 2:
        parameter = sys.argv[1]
    else:
        usage()

    # print md5 hash
    md5_hash = md5sum(parameter)
    print("{}\t{}".format(md5_hash, parameter))


if __name__ == "__main__":
    main()
    exit(0)
