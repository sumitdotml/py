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

parser.add_argument(
    "-print",
    help="print the path of the specified directories, files, or filetypes",
    action="store_true",
)

parser.add_argument(
    "-name",
    help="name pattern to use for searching in the specified directory path",
)

parser.add_argument(
    "-type",
    help="specify whether to filter via filename or dir name or symlinks",
    choices=["d", "f"],  # doing only dir and filename schemes for now
)

parser.add_argument("path", help="specify the target path")

args = parser.parse_args()

if args.type == "d":
    assert os.path.exists(f"{args.path}"), (
        f"find: {args.path}: No such file or directory"
    )
    for dirpath, _, _ in os.walk(top=args.path):
        print(dirpath)

if args.type == "f":
    assert os.path.exists(f"{args.path}"), (
        f"find: {args.path}: No such file or directory"
    )
    for dirpath, _, filenames in os.walk(top=args.path, topdown=True):
        for file in filenames:
            print(get_filenames(file, dirpath))

if args.name:
    [print(f"./{files}") for files in glob.glob(f"**/{args.name}", recursive=True)]

# trying to follow the real `find` tool's convention here:
# basically, if there's: `find .` without any flag specified, it recursively
# prints from the cwd as default.
# following is one way my find.py mimics that
should_print = args.print or not (args.type or args.name)

if should_print:
    assert os.path.exists(f"{args.path}"), (
        f"find: {args.path}: No such file or directory"
    )
    if os.path.isfile(args.path):
        print(args.path)
    else:
        for dirpath, subdirs, filenames in os.walk(top=args.path, topdown=True):
            print(dirpath)
            for file in filenames:
                print(get_filenames(file, dirpath))
