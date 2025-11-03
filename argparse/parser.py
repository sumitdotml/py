import argparse
import subprocess
import random
from pathlib import Path

parser = argparse.ArgumentParser()

# positional arguments
parser.add_argument("x", help="base", type=int)
parser.add_argument("y", help="exponent", type=int)
parser.add_argument("z", help="addition that follows x^y", type=int)

# flag arguments
parser.add_argument(
    "--verbosity", "-v", help="make cli print more verbose", action="count", default=0
)
parser.add_argument(
    "--add", "-a", help="appending file names", action="append", default=None
)
parser.add_argument(
    "--rand", "-r", help="print a random 2-digit number", action="store_true"
)
parser.add_argument("--fish", "-f", help="fish ascii", action="store_true")

# options
parser.add_argument("--day", help="dummy flag 1")
parser.add_argument("--capital", help="dummy flag 2")
parser.add_argument("--fff", help="press f for respect")

# another positional arg
parser.add_argument("files", help="file names", nargs="*")

args = parser.parse_args()

answer = args.x**args.y + args.z

if args.verbosity >= 2:
    print(f"{args.x}^{args.y}+{args.z} equals {answer}.")
elif args.verbosity >= 1:
    print(f"{args.x}^{args.y}+{args.z}={answer}")
else:
    print(answer)

if args.rand:
    print(random.randint(10, 99))

if args.add:
    for item in args.add:
        print(f"Including: {item}")

if args.fish:
    print("""        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´-·¸)
     `\\´´..·´  
    """)

for file_name in args.files:
    file_path = Path(file_name)
    if file_path.suffix == ".py":
        subprocess.run(["python3", file_name])
    else:
        with open(file_name, "r") as file:
            print(file.read())
