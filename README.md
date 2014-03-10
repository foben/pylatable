# PyLaTable

a python script to create simple LateX tables from csv files.

Run python pylatable -h to see the commands:
```
usage: pylatables.py [-h] [-s s] [-d d] [-v v] [-f f] [-a astr]
                     [--no-left-border] [--no-right-border] [--no-top-border]
                     [--no-bottom-border] [--no-between-borders]
                     filename

positional arguments:
  filename              The csv from which to create LateX table

optional arguments:
  -h, --help            show this help message and exit
  -s s, --seperator s   The cell delimiter to use (default: ,)
  -d d, --decimal-places d
                        Number of decimal places for float values (default: 2)
  -v v, --verbatim-marker v
                        The verbatim marker to use. Change if your cells
                        contain the "=" sign (default: =)
  -f f, --float-appendage f
                        Some string to append to floating point numbers
                        (default: )
  -a astr, --alignment-string astr
                        A LateX-like string for aligning columns, . e.g "rlc".
                        Pipes and spaces are ignored (no formatting possible).
                        other unrecognised chararacters and additional,
                        unspecified columns are interpreted as "c" (centered).
                        (default: )
  --no-left-border      Do not print the left border (default: True)
  --no-right-border     Do not print the right border (default: True)
  --no-top-border       Do not print the top border (default: True)
  --no-bottom-border    Do not print the bottom border (default: True)
  --no-between-borders  Do not print the borders between columns (default:
                        True)
```
