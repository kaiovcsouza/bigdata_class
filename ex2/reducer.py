#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

SEP = '\t'


class Reducer(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def reduce(self):
        for current, group in groupby(self, itemgetter(0)):
            try:
                rows = []
                for current, row in group:
                    rows.append(row)
                self.emit(current, rows)
            except ValueError:
                pass

    def __iter__(self):
        for line in self.infile:
            yield line.rstrip().split(self.sep, 1)


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
