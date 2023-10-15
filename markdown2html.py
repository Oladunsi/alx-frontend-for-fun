#!/usr/bin/python3

"""A script that converts a markdown file and then 
    generates a html file as a new file"""

import sys
import os
import re


def markdown2html(source_file_name, generated_file_name):
    if os.path.exist(source_file_name) and os.path.isfile(source_file_name) == False:
        print("Missing <filename>")
        sys.exit(1)
    sys.exit(0)

if __name__ = "__main__":
    if sys.argv != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 )
