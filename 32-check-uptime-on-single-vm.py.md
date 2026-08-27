# SSH Uptime Checker

A simple Python script that connects to a Linux VM using SSH and checks its system uptime with Paramiko.

## Project Structure

```text
check-server-uptime/
├── check_uptime.py
└── venv/
```

## Requirements

- Python 3
- Paramiko
- Linux VM with SSH enabled

## Setup

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Paramiko

```bash
pip install paramiko
```

### 3. Set SSH password

```bash
export SSH_PASSWORD="your-password"
```

Do not store the password in the Python script.

## Code

Create `check_uptime.py`:

```python
import sys
import os
import paramiko


hostname = sys.argv[1]
username = sys.argv[2]

password = os.getenv("SSH_PASSWORD")

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
    print(f"Connection failed: {e}")

finally:
    client.close()
```
![alt text](<Screenshot (641).png>)
## Usage

```bash
python3 check_uptime.py <IP_ADDRESS> <USERNAME>
```

Example:

```bash
python3 check_uptime.py 192.168.1.18 sum
```

## Workflow

```text
IP + Username
      ↓
SSH Connection
      ↓
Run "uptime"
      ↓
Display Result
      ↓
Close Connection
```

## Example Output

```text
[192.168.1.18] 22:10:15 up 2 days, 3:42, 1 user, load average: 0.05, 0.03, 0.01
```

## Screenshot
![alt text](<Screenshot (642)(1).png>)
![alt text](<Screenshot (643).png>)
Add a screenshot of the terminal showing the script execution and output.