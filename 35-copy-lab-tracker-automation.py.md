# GitHub Lab Tracker Automation

## Overview

An automated lab tracking system built with Python, Google Sheets, and the GitHub API.

The script checks student GitHub repositories for assigned lab files and automatically updates the Lab Tracker with the submission status.

## Features

- Automatically checks student GitHub repositories
- Detects assigned lab files
- Updates the Lab Tracker with `Yes` or `No`
- Uses green and red formatting to show submission status
- Processes multiple students and labs automatically
- Uses bulk updates for efficient Google Sheets operations

## Tech Stack

- Python 3
- GitHub REST API
- Google Sheets API
- gspread
- requests
- Google Service Account

## Implementation

The automation is implemented in `googlesheet_lab.py`.


![alt text](<Screenshot (655)-1.png>)
![alt text](<Screenshot (656)-1.png>)
![alt text](<Screenshot (657)-1.png>)
![alt text](<Screenshot (658)-1.png>)
![alt text](<Screenshot (659).png>)
![alt text](<Screenshot (660).png>) 

## Installation

All required Python packages are listed in `requirements.txt`.

Install them using:

    pip3 install -r requirements.txt

## Configuration

The project uses a Google Service Account to access Google Sheets.

Credentials are stored locally in:

    google-credentials.json

A GitHub Personal Access Token is configured using an environment variable:

    export LAB_TRK_PAT="YOUR_GITHUB_TOKEN"

> Do not upload `google-credentials.json` or your GitHub token to GitHub.

## Usage

Run the automation with:

    python3 googlesheet_lab.py

The script connects to Google Sheets, checks the assigned GitHub repositories, and updates the Lab Tracker automatically.

![alt text](<Screenshot (654).png>)

## Result

The final Lab Tracker displays the submission status for each student.

- **Green:** Lab completed
- **Red:** Lab not completed
- **Yes:** Lab file found in the repository
- **No:** Lab file not found in the repository

![alt text](<Screenshot (661).png>)

## Conclusion

This project automates GitHub lab verification and provides a clear visual overview of student submissions through Google Sheets.

**Python + GitHub API + Google Sheets = Automated Lab Tracking**