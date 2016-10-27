#!/usr/bin/env python
"""
Description

Convert text file line endings

     dos2unix  '\r\n' -> '\n'
     mac2unix    '\r' -> '\n'

Usage

        python converteol.py dos2unix file

Note

 - works with python 2.7 and 3.5

Author

  David Laperriere <dlaperriere@outlook.com>
"""
import os
import shutil
import sys

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

copystat = shutil.copystat
ext_backup = '.bak'
ext_converted = '.conv_eol'
backup = True

# Python version compat
if sys.version_info[0] <= 2:
    Py3 = False
elif sys.version_info[0] >= 3:
    Py3 = True


def usage():
    """ Show script parameters """
    print("Usage: converteol.py dos2unix|mac2unix file")
    sys.exit(0)

# newline conversion methods


def dos2mac(data):
    return '\r'.join(data.split('\r\n'))


def dos2unix(data):
    return '\n'.join(data.split('\r\n'))


def mac2dos(data):
    return '\r\n'.join(data.split('\r'))


def mac2unix(data):
    return '\n'.join(data.split('\r'))


def unix2dos(data):
    return '\r\n'.join(data.split('\n'))


def unix2mac(data):
    return '\r'.join(data.split('\n'))


# read/write files
def read_file(filename):
    """read file without converting line endings"""
    if Py3:
        return open(filename, "r", newline='')
    return open(filename, "rb")


def write_file(filename):
    """write file without converting line endings"""
    if Py3:
        return open(filename, "w", newline='')
    return open(filename, "wb")

# MAIN


def main():
    """ Main: check parameters and convert end of lines """

    # check parameters
    if len(sys.argv) >= 3:
        conversion = sys.argv[1]
        files = sys.argv[2:]

        if conversion == "unix2dos":
            convert = unix2dos
        elif conversion == "unix2mac":
            convert = unix2mac
        elif conversion == "dos2mac":
            convert = dos2mac
        elif conversion == "dos2unix":
            convert = dos2unix
        elif conversion == "mac2dos":
            convert = mac2dos
        elif conversion == "mac2unix":
            convert = mac2unix
        else:
            usage()

    else:
        usage()

    # convert eol
    for current_file in files:
        if not os.path.isfile(current_file):
            continue
        backfile = current_file + ext_backup
        newfile = current_file + ext_converted

        with read_file(current_file) as f:
            data = f.read()
            newdata = convert(data)
        with write_file(newfile) as w:
            w.write(newdata)

        copystat(current_file, newfile)
        if os.path.isfile(backfile):
            newbackfile = backfile + ext_backup
            while(os.path.isfile(newbackfile)):
                newbackfile = newbackfile + ext_backup
            os.rename(backfile, newbackfile)
        os.rename(current_file, backfile)
        os.rename(newfile, current_file)

        if not backup:
            if os.path.isfile(backfile):
                os.unlink(backfile)

        print("Converted {}...".format(current_file))

if __name__ == "__main__":
    main()
