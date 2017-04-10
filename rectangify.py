#!/usr/bin/env python
"""
create tables from cell lists
"""

import sys
import os
import csv
import argh
import argparse
import contextlib


#
# IO helpers
#
@contextlib.contextmanager
def smart_open(fname=None, mode='r'):
    if fname and fname != '-':
        fh = open(fname, mode)
        close_me = True
    else:
        if mode is None or 'r' in mode:
            fh = sys.stdin
        else:
            fh = sys.stdout
        close_me = False

    try:
        yield fh
    finally:
        if close_me:
            fh.close()


def from_colslist(lines, out, marker):
    """
    Create tables from a list of columns in `lines`; write to `out`.
    - The columns consist of each cell on one line.
    - The columns follow each other in the list.
    - The columns are separated by a line with a marker string
    - The first column *can* have the marker string on top.
    """
    if lines[0] != marker:
        lines.insert(0, marker)

    # distribute to columns
    cols = []
    for l in lines:
        if l == marker:
            cols.append([])
            continue

        col = cols[-1]
        col.append(l)

    # output columns
    with smart_open(out, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        i_row = 0
        while True:
            line_added = False
            row_out = []
            for col in cols:
                val = ""
                if i_row < len(col):
                    val = col[i_row]
                    line_added = True
                row_out.append(val)
            if not line_added:
                break
            csvwriter.writerow(row_out)
            i_row += 1


def insert_markers(lines, row_num, marker):
    """ Insert markers every `row_num` lines"""
    for i in range(len(lines)-row_num, 0, -1*row_num):
        lines.insert(i, marker)

MARKER_DEFAULT = '---'
argh.PARSER_FORMATTER = argparse.RawDescriptionHelpFormatter
@argh.arg('INPUT', help="input file (or '-' for stdin)")
@argh.arg('-o', '--out', help="save output in file OUT instead of stdout")
@argh.arg('-m', '--marker',
          help="marker designating the start of a new column " +
               "(default: '%(default)s')",
          metavar='STR')
@argh.arg('-r', '--rows',
          help="number of rows (instead of marker) - " +
               "NOT SUPPORTED YET!",
          metavar='NUM')

def rectangify(INPUT, out=None, marker=MARKER_DEFAULT, rows=None):
    """Create tables from cell lists
    """
    with smart_open(INPUT, 'r') as inpfile:
        lines = inpfile.read().splitlines()

    if rows:
        row_num = int(rows)
        marker = MARKER_DEFAULT
        insert_markers(lines, row_num, marker)

    from_colslist(lines,out,marker)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        formatter_class=argh.PARSER_FORMATTER)
    argh.set_default_command(parser, rectangify)
    argh.dispatch(parser)

