import sys
import argparse
import re

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('filename', help='The csv from which to create LateX table')
    parser.add_argument('-s', '--seperator', metavar='s', type=str, default=',',\
            help='The cell delimiter to use')
    parser.add_argument('-d', '--decimal-places', metavar='d', type=int, default=2,\
            help='Number of decimal places for float values')
    parser.add_argument('-v', '--verbatim-marker', metavar='v', type=str, default='=',\
            help='The verbatim marker to use. Change if your cells contain the "=" sign')
    parser.add_argument('-f', '--float-appendage', metavar='f', type=str, default='',\
            help='Some string to append to floating point numbers')
    parser.add_argument('-a', '--alignment-string', metavar='astr', type=str, default='',\
            help='A LateX-like string for aligning columns, . e.g "rlc".\n \
            Pipes and spaces are ignored (no formatting possible).\n \
            other unrecognised chararacters and additional,\n \
            unspecified columns are interpreted as "c" (centered).')

    parser.add_argument('--no-left-border', action='store_false',
            help='Do not print the left border')
    parser.add_argument('--no-right-border', action='store_false',
            help='Do not print the right border')
    parser.add_argument('--no-top-border', action='store_false',
            help='Do not print the top border')
    parser.add_argument('--no-bottom-border', action='store_false',
            help='Do not print the bottom border')
    parser.add_argument('--no-between-borders', action='store_false',
            help='Do not print the borders between columns')


    args = parser.parse_args()

    filename = args.filename
    seperator = args.seperator
    decimal_places = args.decimal_places
    float_appendage = args.float_appendage.replace('%', '%%')
    verbatim_marker = args.verbatim_marker
    alignment_string = args.alignment_string
    
    create_latex_table(filename, seperator=seperator, decimal_places=decimal_places, \
            float_appendage=float_appendage, verbatim_marker=verbatim_marker,
            alignment_string=alignment_string,
            border_left=args.no_left_border,
            border_right=args.no_right_border,
            border_top=args.no_top_border,
            border_bottom=args.no_bottom_border,
            border_between=args.no_between_borders)

def create_latex_table(filename, seperator=',', decimal_places=2, float_appendage='', verbatim_marker='=',
        alignment_string='',
        border_left=True, border_right=True, border_top=True, border_bottom=True, border_between=True):

    verb = '\\verb' + verbatim_marker + '%s' + verbatim_marker
    verbfl = '\\verb' + verbatim_marker + '%.' + str(decimal_places) + 'f' + float_appendage + verbatim_marker

    alignment_string = alignment_string.replace('|','').replace(' ','')
    alignment_string = re.sub(r"[^rlc]{1,1}", "c", alignment_string)

    input_file = open(filename, "r")

    firstline = input_file.readline()
    field_count = len(firstline.split(seperator))
    input_file.seek(0)

    write_begin(field_count, 
            border_left=border_left, border_right=border_right, border_between=border_between,
            alignment_string=alignment_string)

    if border_top: print '\\hline'

    for input_line in input_file.readlines():
        tline = ''
        input_line = input_line.rstrip()
        fields = input_line.split(seperator)
        no_fields = len(fields)

        for fi in range(no_fields):
            isfloat = False
            isint = False

            ##Check if its maybe a float
            try:
                float(fields[fi])
                isfloat = True
            except ValueError:
                pass

            ## Add verbatized cell to prevent errors
            if isfloat:
                tline += verbfl % float(fields[fi])
            else:
                tline += verb % fields[fi]


            ## Add field seperator if not last cell in row
            if fi < no_fields - 1:
                tline += ' & '

        tline += ' \\\\'
        print tline

    if border_bottom: print '\\hline'
    write_end()

def write_begin(field_count, alignment_string='', border_left=True, border_right=True, border_between=True ):
    tablehead = '\\begin{tabular}{'
    if border_left: tablehead += ' | '
    for i in range(field_count):
        if i + 1 <= len(alignment_string):
            tablehead += ' %s ' % alignment_string[i]
        else:
            tablehead += ' c '
        if border_between and i < field_count - 1:
            tablehead += '|'
    if border_right: tablehead += ' | '
    tablehead += '}'
    print tablehead

def write_end():
    print '\\end{tabular}'

main()
