#!/usr/bin/env python
"""
create tables from cell lists
"""

import sys
import csv
import argh
import argparse
import time
import contextlib

COLS_MODE = 'COLS'
ROWS_MODE = 'ROWS'

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


def from_rowslist(lines, out, marker):
    """
    Create tables from a list of rows in `lines`; write to `out`.
    - The rows consist of each cell on one line.
    - The rows follow each other in the list.
    - The rows are separated by a line with a marker string
    - The first row *can* have the marker string on top.
    """
    # distribute to rows
    rows = []
    cols_max = 0
    for l in lines:
        if l == marker:
            rows.append([])
            continue

        r = rows[-1]
        r.append(l)
        cols_max = max([cols_max, len(r)])

    # fill rows
    for r in rows:
        r += [''] * (cols_max - len(r))

    # output rows
    with smart_open(out, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        for r in rows:
            csvwriter.writerow(r)


def make_magic_marker():
    """generate a unique marker string (time based)"""
    return "---" + str(time.time()) + "---"

def insert_markers(lines, item_num, marker):
    """ Insert markers every `item_num` lines"""
    for i in range(len(lines)-item_num, 0, -1*item_num):
        lines.insert(i, marker)

argh.PARSER_FORMATTER = argparse.RawDescriptionHelpFormatter
#argh.PARSER_FORMATTER = argparse.RawTextHelpFormatter
@argh.arg('INPUT', help="input file (or '-' for stdin)")
@argh.arg('-c', '--convert',
          help="convert mode to use: " +
                "'"+COLS_MODE+"' (cells of one column are listed together) " +
                "or '"+ROWS_MODE+"' (cells of one row are listed together). " +
                "(default: '%(default)s')",
          choices=[COLS_MODE, ROWS_MODE], type = str.upper)
@argh.arg('-o', '--out', help="save output in file OUT instead of stdout")
@argh.arg('-m', '--marker',
          help="marker line designating the start of a new column/row " +
               "(without the newline)." +
               "(default: '%(default)s')",
          metavar='STR')
@argh.arg('-i', '--items',
          help="number of items until the next column/row starts " +
               "(has precedence over marker)",
          metavar='NUM')
def rectangify(INPUT, convert=COLS_MODE, out=None, marker='---', items=None):
    """create CSV tables from a list of columns/rows"""
    with smart_open(INPUT, 'r') as inpfile:
        lines = inpfile.read().splitlines()

    if items:
        item_num = int(items)
        marker = make_magic_marker()
        insert_markers(lines, item_num, marker)

    if lines[0] != marker:
        lines.insert(0, marker)

    if convert==COLS_MODE:
        from_colslist(lines, out, marker)
    elif convert==ROWS_MODE:
        from_rowslist(lines, out, marker)
    else:
        raise argh.CommandError(
            "Convert mode '{0}' not available".format(convert))

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argh.PARSER_FORMATTER)
    argh.set_default_command(parser, rectangify)
    argh.dispatch(parser)
    
if __name__ == '__main__':
    main()
