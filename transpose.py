#!/usr/bin/env python
"""
Description

Transpose text file columns and rows


Usage

        python transpose.py file
        gunzip -c file.gz | python transpose.py -

Note

 - works with python 2.7 and 3.6

Author

  David Laperriere <dlaperriere@outlook.com>
"""
from __future__ import print_function

import itertools
import os
import sys
import tempfile

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

missing_value = "NA"
sep = '\t'


def usage():
    print("Usage: python transpose.py file")
    sys.exit(-1)


def read_file(tsv_file):
    """read file or stdin"""
    if(tsv_file == "-" or tsv_file == "stdin"):
        return sys.stdin
    return open(tsv_file, 'rU')

# Python version compat
if sys.version_info[0] <= 2:
    Py3 = False
elif sys.version_info[0] >= 3:
    Py3 = True


def zipl(*lis):
    """ Python 2/3 zip_longest """
    if(Py3):
        return itertools.zip_longest(*lis, fillvalue=missing_value)

    return itertools.izip_longest(*lis, fillvalue=missing_value)


# MAIN


def main():
    """ Main check parameters & transpose file """

    # check parameters
    if len(sys.argv) >= 2:
        afile = sys.argv[1]
    else:
        print("Usage: python transpose.py file")
        sys.exit(0)

    # replace blanks
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmpfile = tmp.name
    with read_file(afile) as f:
        data = f.read()
        data = data.replace(sep + sep, sep + missing_value + sep)
        data = data.replace('\n' + sep, '\n' + missing_value + sep)
        with open(tmpfile, 'w') as w:
            w.write(data)

    # transpose rows and columns
    with read_file(tmpfile) as f:
        lis = [x.split() for x in f]
    for x in zipl(*lis):
        print(sep.join(x))

    tmp.close()
    os.unlink(tmpfile)

if __name__ == "__main__":
    main()
