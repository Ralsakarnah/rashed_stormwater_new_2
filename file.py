import os
import logging
from flask import Flask, jsonify, render_template, url_for
from gs import get_google_sheet_data  # Import the function

# Initialize Flask app
app = Flask(__name__)

# Enable debug mode
app.debug = True

# Setup logging to console
logging.basicConfig(level=logging.DEBUG)

# Route for index page
@app.route('/')
def index():
    app.logger.debug("Serving index.html")
    return render_template('index.html')

# Route to fetch data from Google Sheets API
@app.route('/api/data', methods=['GET'])
def get_data():
    df = get_google_sheet_data()  # Fetch the data from Google Sheets
    
    # Log to confirm data fetching
    app.logger.debug(f"Fetched data: {df.head()}")

    # Prepare the data for JSON response
    response_data = df.to_dict(orient='records')
    return jsonify(response_data)

# Logging to track static files
@app.route('/static/<path:filename>')
def static_file(filename):
    app.logger.debug(f"Requesting static file: {filename}")
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
