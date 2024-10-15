import os
from flask import Flask, jsonify, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json  # Import for reading JSON from environment variable

app = Flask(__name__)

# Set up the Google Sheets API using credentials from environment variable
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Open Google Sheet and get data
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/e/2PACX-1vRhcARj557XHf_PaANggXNm55G0AdTQ16lkQvIiJhiOg1LHkK0jBTtW48Yae1Ds81Yjqc6ne0bd2haA/pubhtml")
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_all_records()

    # Convert data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Prepare the data for JSON response
    response_data = []
    for _, row in df.iterrows():
        response_data.append({
            'date': row['date'],
            'time': row['time'],
            'depth': row['depth']  # Assuming your column name is 'depth'
        })

    return jsonify(response_data)

# Use os to get the PORT from the environment, default to 10000 if not provided
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
