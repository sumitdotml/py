All the files and directories in this `find/` directory are dummies, except for the `find.py` file.

These are all for testing the `file.py` file's capability to recreate the `find` tool.

Trying to implement 3 main arguments for now: `-name`, `-print`, and `-type`.

## Module Reference

### subprocess

The `subprocess` module lets our Python program run external commands - like executing `ls`, `git`, `grep`, or any other program from within our script.

**What it's for:**

- Running external programs/commands from inside Python
- Capturing output from those commands
- Automating workflows that involve multiple tools
- Testing command-line tools (like our find implementation)

**Example use cases:**

```python
import subprocess

subprocess.run(['ls', '-la'])
subprocess.run(['git', 'status'])

# capturing output
result = subprocess.run(['echo', 'hello'], capture_output=True, text=True)
print(result.stdout)

result = subprocess.run(['python', 'find.py', '.', '-name', '*.py'],
                       capture_output=True, text=True)
```

**Note:** Don't think I'll need subprocess IN my find.py implementation itself. I'd probably use it to TEST my implementation from another script.

### glob

The `glob` module finds files matching wildcard patterns - like shell wildcards but in Python.

**What it does:**

- Takes a pattern with wildcards and returns matching file paths
- `*` matches any characters
- `**` matches directories recursively (with `recursive=True`)
- `?` matches a single character
- Returns both files and directories (doesn't distinguish)

**What it doesn't do:**

- Doesn't filter by file type (file vs directory)
- Doesn't provide the same traversal control as find
- Just pattern matching, not full search capabilities

**Examples:**

```python
import glob

glob.glob('*.py')                           # ['find.py', 'setup.py']
glob.glob('src/*.py')                       # ['src/main.py']
glob.glob('**/*.py', recursive=True)        # All .py files recursively
glob.glob('**/test_*.py', recursive=True)   # All test files recursively
```

### os

The `os` module provides functions to interact with the operating system - particularly for working with files, directories, and paths.

**What it's for:**

- Navigating the file system
- Checking file and directory properties
- Building and manipulating file paths
- Listing directory contents
- Traversing directory trees

**Key components:**

#### `os.path` - Path operations

```python
import os

os.path.isfile('data.txt')      # True if it's a file
os.path.isdir('src')            # True if it's a directory
os.path.exists('README.md')     # True if it exists

os.path.basename('./src/main.py')    # Returns: 'main.py'
os.path.dirname('./src/main.py')     # Returns: './src'

# build paths safely (handles / or \ depending on OS)
os.path.join('src', 'utils', 'helper.py')  # 'src/utils/helper.py'
```

#### `os.listdir()` - List directory contents

```python
# getting all items in a directory (non-recursive)
os.listdir('.')
# returns: ['find.py', 'README.md', 'src', 'tests', 'data.txt', ...]

os.listdir('./src')
# returns: ['main.py', 'utils']
```

#### `os.walk()` - Recursively traverse directories

```python
# walking through directory tree
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"Currently in: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"Files: {filenames}")

# Example output:
# Currently in: .
# Subdirectories: ['src', 'tests', 'docs']
# Files: ['find.py', 'README.md', 'data.txt', ...]
#
# Currently in: ./src
# Subdirectories: ['utils']
# Files: ['main.py']
#
# Currently in: ./src/utils
# Subdirectories: []
# Files: ['helper.py', 'parser.py']
```

- `os.walk()` gives us recursive directory traversal
- `os.path.isfile()` and `os.path.isdir()` let us filter by type
- `os.path.basename()` gives us just the filename for pattern matching
- `os.path.join()` helps build correct paths
