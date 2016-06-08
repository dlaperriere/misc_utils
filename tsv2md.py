#!/usr/bin/env python
"""
Description

Create markdown table from the beginning of a tsv file

Usage

        python tsv2md.py --file name [--line 1 --transpose]

Note

 - works with python 2.7 and 3.5

Author

  David Laperriere <dlaperriere@outlook.com>
"""
import argparse
import textwrap

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

sep = "\t"
md_sep = " | "


def build_argparser():
    """ Build command line arguments parser """
    parser = argparse.ArgumentParser(
        prog=__file__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
      Create markdown table from the beginning of a tsv file
                               '''),
        epilog=textwrap.dedent('''
    Example

       python tsv2md.py --file name [--line 1 --transpose]

        ''')
    )
    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None,
                        help='tsv file')
    parser.add_argument('-l', '--line',
                        type=int,
                        required=False,
                        default=1,
                        help='line to include in markdown table')
    parser.add_argument('-t', '--transpose',
                        action='count',
                        required=False,
                        default=0,
                        help='print columns as rows')

    parser.add_argument('-v', '--version', action='version',
                        version="%(prog)s v" + __version__)

    return parser


def main():
    """ Main: parse arguments and print markdown table """

    # parse command line arguments
    parser = build_argparser()
    pyargs = parser.parse_args()

    # read tsv file
    line_count = 0
    for line in pyargs.file:
        line = line.strip()
        if line_count == 0:
            header = line.split(sep)
        else:
            tsv_line = line.split(sep)
            if line_count == pyargs.line:
                break
        line_count += 1

    # print markdown table
    header_len = list(map(len, header))
    tsv_len = list(map(len, tsv_line))
    header_line = list()

    if pyargs.transpose > 0:
        # transpose columns as rows
        col_max_length = max(header_len)
        ex_max_length = max(tsv_len)
        theader = ["column" + " " * (col_max_length - len("column")),
                   "example" + " " * (ex_max_length - len("example"))]
        theader_line = ["-" * col_max_length, "-" * ex_max_length]

        print(md_sep.join(theader))
        print(md_sep.join(theader_line))
        for col, ex in zip(header, tsv_line):
            col = col + " " * (col_max_length - len(col))
            ex = ex + " " * (ex_max_length - len(ex))
            print(col + md_sep + ex)

    else:
        # as is
        for i in range(0, len(header)):
            max_length = max(header_len[i], tsv_len[i])
            header[i] = header[i] + " " * (max_length - len(header[i]))
            header_line.append("-" * max_length)
            tsv_line[i] = tsv_line[i] + " " * (max_length - len(tsv_line[i]))

        print(md_sep.join(header))
        print(md_sep.join(header_line))
        print(md_sep.join(tsv_line))
    print("")
    print("")

if __name__ == "__main__":
    main()
    exit(0)
