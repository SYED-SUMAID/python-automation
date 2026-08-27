# Multi-VM SSH Uptime Checker

A Python automation tool that connects to multiple Linux virtual machines over SSH and retrieves their system uptime using Paramiko.

## Overview

The script reads VM IP addresses from a file, connects to each VM using SSH, executes the `uptime` command, and displays the result.

```text
IP Address File
      ↓
Read IPs
      ↓
SSH Connection
      ↓
Run uptime
      ↓
Display Result
```

## Project Structure

```text
check-server-uptime/
├── check_uptime.py
├── ips.txt
└── venv/
```

## Requirements

- Python 3
- Paramiko
- Linux VMs with SSH enabled
- Network access to the VMs
- A valid SSH username and password

## Setup

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install the Required Dependency

```bash
pip install paramiko
```

The Python standard-library modules `sys` and `os` do not require installation.

### 3. Required Python Modules

The script imports:

```python
import sys
import os
import paramiko
```

| Module | Purpose |
|---|---|
| `sys` | Handles command-line arguments |
| `os` | Reads the SSH password from an environment variable |
| `paramiko` | Creates and manages SSH connections |

## Configuration

### IP Address File

Create `ips.txt` and add one VM IP address per line:

```text
192.168.1.18
192.168.1.19
192.168.1.20
192.168.1.21
```

![alt text](<Screenshot (638).png>)

### SSH Password

Set the SSH password as an environment variable:

```bash
export SSH_PASSWORD="your-password"
```

The password is kept outside the Python source code.

## Usage

Run the script with the IP file and SSH username:

```bash
python check_uptime.py ips.txt sum
```

| Argument | Description |
|---|---|
| `ips.txt` | File containing VM IP addresses |
| `sum` | SSH username |

**Screenshot:** Add a screenshot of the terminal command and output here.

## Python Script

```python
import sys
import os
import paramiko


def read_ips(filename):
    with open(filename, "r") as file:
        return [ip.strip() for ip in file if ip.strip()]


ip_file = sys.argv[1]
username = sys.argv[2]

password = os.getenv("SSH_PASSWORD")

ips = read_ips(ip_file)


for hostname in ips:

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname,
            username=username,
            password=password
        )

        stdin, stdout, stderr = client.exec_command("uptime")

        output = stdout.read().decode().strip()

        print(f"[{hostname}] {output}")

    except Exception as e:
        print(f"[{hostname}] Connection failed: {e}")

    finally:
        client.close()
```

![alt text](<Screenshot (639).png>)

## Execution Flow

```text
Start
  ↓
Read command-line arguments
  ↓
Read SSH password
  ↓
Read IP addresses from ips.txt
  ↓
Loop through each IP
  ↓
Connect using SSH
  ↓
Execute "uptime"
  ↓
Display result
  ↓
Close SSH connection
  ↓
Next VM
```

## Example Output

```text
[192.168.1.18] 22:10:15 up 2 days, 3:42
[192.168.1.19] 22:10:18 up 5 days, 1:32
[192.168.1.20] 22:10:21 up 1 day, 7:44
```

## Security

Do not commit passwords, private keys, or other credentials to GitHub.

Use environment variables or SSH keys for authentication.