#! /usr/bin/env python
""" How important is heritability to Darwin's
Theory of Natural Selection?

In this script we will find out!

Parameters:
    infile: argument 1 (Origin of Species)
    outfile: argument 2 (line numbers and occurances)

Remember: The concept of heritability can be
written in many ways. Such as:
    Inheritance
    Inherited
    Heritability
    Heritable
"""

import re
import sys


def reportOccurance(REpattern_obj, line, line_index, outfile):
    """This function uses a pre-defined regex
    object to search a line. If the pattern matches
    a string, the string will be printed to the 
    outfile along with the line number.
    REpattern_obj: regular expression object
    line: string to be searched
    line_num: line number of document being searched
    outfile: where results will be written
    """
    if REpattern_obj.search(line):
        outfile.write(str(line_index + 1) + "\t" + REpattern_obj.search(line).group() + "\n")

if __name__ == '__main__':
    REpattern_string = r'\w+herit\w+'
    REpattern_obj = re.compile(REpattern_string, re.IGNORECASE)
    with open(sys.argv[1], 'r') as instream:
        with open(sys.argv[2], 'w') as outstream:
            for line_index, line in enumerate(instream):
                if "***" not in line:
                    reportOccurance(REpattern_obj, line.strip(), line_index, outstream)


