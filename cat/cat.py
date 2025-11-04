"""
simple reimplementation of the `cat` command
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filenames", help="file name to output the input of", nargs="*")

parser.add_argument(
    "-n", help="number the output lines, starting at 1", action="store_true"
)

args = parser.parse_args()

for filename in args.filenames:
    with open(filename, "r") as file:
        if args.n:
            for i, line in enumerate(file):
                print(f"     {i + 1}  {line.rstrip()}")
        else:
            print(file.read())
