#!/usr/bin/env python
"""
Description

Apply a command in parallel to a list of file

Usage

        python parallel_cmd.py --command cmd --files list [--thread  2]

Note

 - works with python 2.7 and 3.5
 - gnu parallel and xargs have more options

Author

  David Laperriere <dlaperriere@outlook.com>
"""
from __future__ import print_function

import argparse
import itertools
import multiprocessing
import os
import sys
import textwrap

from lib import cmd

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

cpu = multiprocessing.cpu_count()


def build_argparser():
    """ Build command line arguments parser """
    parser = argparse.ArgumentParser(
        prog=__file__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
      Apply a command in parallel to a list of file
                               '''),
        epilog=textwrap.dedent('''
    Example

       python parallel_cmd.py --command cmd --files list [--thread 2]
       ls *.txt |  python parallel_cmd.py --command gzip --files -

        ''')
    )
    parser.add_argument('-c', '--command',
                        type=str,
                        required=True,
                        default="#",
                        help='command to run')
    parser.add_argument('-f', '--files',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None,
                        help='list of files')
    parser.add_argument('-t', '--thread',
                        type=int,
                        required=False,
                        default=2,
                        help='number of file to process in parallel')

    parser.add_argument('-v', '--version', action='version',
                        version="%(prog)s v" + __version__)

    return parser


def runCommand(params):
    """Run command with file as parameter"""
    command, file = params
    command_line = command + " " + file
    out, status = cmd.run(command_line)
    print("# " + command_line + ":", file=sys.stderr)
    print(out, file=sys.stdout)


def main():
    """ Main: parse arguments and run command in parallel"""

    # parse command line arguments
    parser = build_argparser()
    pyargs = parser.parse_args()

    if pyargs.thread is not None:
        cpu = pyargs.thread
        if pyargs.thread > multiprocessing.cpu_count():
            cpu = multiprocessing.cpu_count()

    command = pyargs.command

    # read list of files
    files = list()
    for line in pyargs.files:
        line = line.strip()
        if os.path.exists(line):
            files.append("\"" + line + "\"")

    # run command in parallel
    pool = multiprocessing.Pool(cpu)
    params = zip(itertools.repeat(command, len(files)), files)

    pool.map(runCommand, params)

    print("")

if __name__ == "__main__":
    main()
    exit(0)
