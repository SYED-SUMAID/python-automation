# Python Package Checker

A simple Python automation project that checks whether a Python package is installed using Python's `sys` and `subprocess` modules.

## Objective

To check the installation status and basic information of Python packages directly from the terminal.

## Requirements

- Python 3.x
- pip

## Python Code

```python
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python package_checker.py <package_name>")
    sys.exit()

package = sys.argv[1]

result = subprocess.run(
    ["pip", "show", package],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"{package} is installed")
    print(result.stdout)
else:
    print(f"{package} is not installed")
```

## How to Run

Run the script from the terminal:

```bash
python package_checker.py requests
```

Other examples:

```bash
python package_checker.py numpy
python package_checker.py gTTS
python package_checker.py pandas
```

## Example Output

```text
requests is installed
Name: requests
Version: 2.x.x
Location: C:\...\site-packages
```

For a package that is not installed:

```text
abcxyz is not installed
```

If no package name is provided:

```text
Usage: python package_checker.py <package_name>
```

## Modules Used

### `sys`

`sys.argv` is used to receive the package name from the command line.

```python
package = sys.argv[1]
```

### `subprocess`

`subprocess.run()` is used to execute the `pip show` command and capture its output.

```python
subprocess.run(
    ["pip", "show", package],
    capture_output=True,
    text=True
)
```

## Working

```text
Package Name
     ↓
  sys.argv
     ↓
 subprocess
     ↓
  pip show
     ↓
Package Information
```
![alt text](<Screenshot (649).png>)


