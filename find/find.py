"""
my implementation of the Unix find command in Python.

currently supports 3 main args:
    -name: pattern matching for file/directory names (supports wildcards like *.py, ❤️ to glob)
    -type: filter by type (f=file, d=directory)
    -print: explicitly print results (this also is the default condition if no args are used)

usage examples:
    python find.py .                    # print everything recursively
    python find.py . -type f            # print only files
    python find.py . -name "*.py"       # find all .py files
    python find.py ./src -type f -name "*.py"  # combine filters

glob used for pattern matching when -name is specified, and recursive traversal for other cases handled by os.walk 🫶.
"""

import argparse
import os
import glob


# helper function
def get_filenames(filename: str, dirpath: str):
    if len(filename) == 0:
        pass
    else:
        return f"{dirpath}/{filename}"


parser = argparse.ArgumentParser()

# -print is an action flag (defaults to False when not specified)
parser.add_argument(
    "-print",
    help="print the path of the specified directories, files, or filetypes",
    action="store_true",
)

# -name takes a pattern (like "*.py" or "test*")
parser.add_argument(
    "-name",
    help="name pattern to use for searching in the specified directory path",
)

# -type filters by file type: d=directory, f=file
parser.add_argument(
    "-type",
    help="specify whether to filter via filename or dir name or symlinks",
    choices=["d", "f"],  # doing only dir and filename schemes for now
)

# path is required (mimicking real find behavior)
parser.add_argument("path", help="specify the target path")

args = parser.parse_args()

# case 1: filtering for directories
if args.type == "d":
    if args.name:
        [
            print(dir)
            for dir in glob.glob(f"{args.path}/**/{args.name}", recursive=True)
            if os.path.isdir(dir)
        ]

    else:
        for dirpath, _, _ in os.walk(top=args.path):
            print(dirpath)

# case 2: filtering for files
elif args.type == "f":
    if args.name:
        [
            print(file)
            for file in glob.glob(f"{args.path}/**/{args.name}", recursive=True)
            if os.path.isfile(file)
        ]
    else:
        for dirpath, _, filenames in os.walk(top=args.path, topdown=True):
            for file in filenames:
                print(get_filenames(file, dirpath))

# case 3: pattern specified but no type filter (shows both files and dirs)
elif args.name and not args.type:
    [print(files) for files in glob.glob(f"{args.path}/**/{args.name}", recursive=True)]

# case 4: default behavior (no filters specified, or just -print)
# trying to follow the real `find` tool's convention here:
# basically, if there's: `find .` without any flag specified, it recursively
# prints from the cwd as default.
else:
    assert os.path.exists(f"{args.path}"), (
        f"find: {args.path}: No such file or directory"
    )
    # if path is a single file, just print it
    if os.path.isfile(args.path):
        print(args.path)
    # otherwise, recursively printing every dir and file
    else:
        for dirpath, subdirs, filenames in os.walk(top=args.path, topdown=True):
            print(dirpath)
            for file in filenames:
                print(get_filenames(file, dirpath))
