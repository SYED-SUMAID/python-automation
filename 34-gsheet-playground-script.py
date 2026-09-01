import os
import gspread
import requests
from google.oauth2.service_account import Credentials

# ==========================================
# 1. CONNECT TO GOOGLE SHEETS
# ==========================================

print("Connecting to Google Sheets...")

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "google-credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1o7WJnJbegdxBkv4kCjTlJslXw0KyiSYMibV-bpPPHhc"
).sheet1

print("Connected!")

# ==========================================
# 2. READ DATA
# ==========================================

print("\nReading Google Sheet...")

name = sheet.acell("B6").value
github_url = sheet.acell("I1").value

print("Name:", name)
print("GitHub:", github_url)


# ==========================================
# 3. GET GITHUB USERNAME
# ==========================================

username = github_url.rstrip("/").split("/")[-1]

print("\nGitHub username:", username)

# ==========================================
# 4. CHECK GITHUB REPOSITORY
# ==========================================

repo_name = "shell-scripting"

url = f"https://api.github.com/repos/{username}/{repo_name}"

response = requests.get(url)

print("\nRepository status:", response.status_code)

if response.status_code == 200:
    print("Repository exists!")
else:
    print("Repository not found.")

# ==========================================
# 5. GET REPOSITORY FILES
# ==========================================

if response.status_code == 200:

    files_url = f"{url}/contents"
    response = requests.get(files_url)

    files = response.json()

    print("\nFiles in repository:")

    for file in files:
        print(file["name"])

# ==========================================
# 6. WRITE RESULT TO GOOGLE SHEET
# ==========================================

sheet.update_acell("B1", "Checked by Python")

print("\nI1 updated!")