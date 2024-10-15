import os
import gspread
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
    # Open the Google Sheet by URL
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/e/2PACX-1vRhcARj557XHf_PaANggXNm55G0AdTQ16lkQvIiJhiOg1LHkK0jBTtW48Yae1Ds81Yjqc6ne0bd2haA/pubhtml")
    worksheet = sheet.get_worksheet(0)  # Open the first worksheet

    # Get all records from the sheet
    data = worksheet.get_all_records()
    return pd.DataFrame(data)
