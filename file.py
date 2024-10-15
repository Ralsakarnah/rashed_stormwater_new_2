from flask import Flask, jsonify, render_template
from gs import get_google_sheet_data  # Import the function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    df = get_google_sheet_data()  # Fetch the data from Google Sheets
    
    # Prepare the data for JSON response
    response_data = df.to_dict(orient='records')
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
