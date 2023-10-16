#!/usr/bin/python3

"""A script that converts a markdown file and then 
    generates a html file as a new file"""

import sys
import os
import re
import haslib


def markdown2html(source_file_name, generated_file_name):
    if os.path.exist(source_file_name) and os.path.isfile(source_file_name) == False:
        print("Missing {}".format(source_file_name))
        sys.exit(1)

    with open(source_file_name) as markdown:
        with open(generated_file_name, 'w') as html:
            ul_start, ol_start, paragraph = False, False, False

            for line in markdown:
                # handling bold fonts
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)
                # handling md5
                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inner = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inner[0].encode()).hexdigest())

                # remove letter c
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_more_c = re.findall(r'\(\((.+?)\)\)', line)
                if remove_letter_c:
                    remove_more_c = ''.join(
                        c for c in remove_more_c[0] if c not in 'Cc')
                    line = line.replace(remove_letter_c[0], remove_more_c)


                # handling header tags
                headings = line.lstrip('#')
                heading_num = len(line) - len(headings)
                # handling unordered list tags
                ul = line.lstrip('-')
                ul_num = len(line) - len(ul)
                # handling ordered list tags
                ol = line.lstrip('*')
                ol_num = len(line) - len(ol)

                # slotting in the header tags
                if 1 <= heading_num <= 6:
                    line = '<h{}>'.format(
                        heading_num) + headings.strip() + '</h{}>'.format(
                        heading_num)
                
                # slotting in the unordered list tags
                if ul_num:
                    if not ul_start:
                        html.write('<ul>\n')
                        ul_start = True
                    line = '<li>' + ul.strip() + '</li>\n'
                if ul_start and not ul_num:
                    html.write('<ul>\n')
                    ul_start = False

                # slotting in the ordered list tags
                if ol_num:
                    if not ol_start:
                        html.write('<ol>\n')
                        ol_start = True
                    line = '<li>' + ol.strip() + '</li>\n'
                if ol_start and not ol_num:
                    html.write('<ol>\n')
                    ol_start = False

                # handling paragraph and brake line
                if not(heading_num or ul_start or ol_start):
                    if not (paragraph and len(line) > 1):
                        html.write('<p>\n')
                        paragraph = True
                    elif len(line) > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False
                if len(line) > 1:
                    html.write(line)
            if ul_start:
                html.write('</ul>\n')
            if ol_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')


if __name__ = "__main__":
    if sys.argv != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    markdown2html(input_file, output_file)    
    sys.exit(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     )
