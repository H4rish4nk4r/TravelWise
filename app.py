from flask import Flask, render_template, jsonify, request,send_from_directory
from flask_cors import CORS

app = Flask(__name__,static_folder='client/public')
CORS(app)

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.get_json()

    # Access the submitted data from the React frontend
    source = data['source']
    destination = data['destination']
    startDate = data['startDate']
    endDate = data['endDate']
    travel = data['travel']
    accommodation = data['accommodation']

    # Perform necessary operations with the data
    # Generate suggestions for travel and accommodation
    travel_suggestions = ['Suggestion 1', 'Suggestion 2', 'Suggestion 3']
    accommodation_suggestions = ['Suggestion A', 'Suggestion B', 'Suggestion C']

    # Prepare the response data
    response_data = {
        'source': source,
        'destination': destination,
        'startDate': startDate,
        'endDate': endDate,
        'travel': travel,
        'accommodation': accommodation,
        'travelSuggestions': travel_suggestions,
        'accommodationSuggestions': accommodation_suggestions
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
