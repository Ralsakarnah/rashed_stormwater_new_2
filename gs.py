import os
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope for Google Sheets and Google Drive
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load Google credentials from environment variable
google_credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')

# Parse the JSON from the environment variable
if google_credentials_json:
    creds_dict = json.loads(google_credentials_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
else:
    raise ValueError("Google credentials not found in environment")

def get_google_sheet_data():
    try:
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1DAF8vwF2-2SedpmdOa-qycuYarnArRGFzWaDx-4dicc/edit?gid=634803012#gid=634803012")
        worksheet = sheet.get_worksheet(0)  # Open the first worksheet
        data = worksheet.get_all_records()
        print(f"Fetched data from Google Sheets: {data}")  # Add this line to log data
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error fetching data from Google Sheets: {str(e)}")
        return pd.DataFrame()

