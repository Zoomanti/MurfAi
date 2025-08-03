# app.py
# Import necessary modules from Flask
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__, static_folder='static', template_folder='templates')

# Define a route for the root URL ('/')
@app.route('/')
def index():
    """
    This function handles requests to the root URL.
    It renders and returns the 'index.html' template.
    """
    return render_template('index.html')

# This block ensures the server runs only when the script is executed directly
if __name__ == '__main__':
    # Run the app in debug mode for development
    # Host '0.0.0.0' makes it accessible on your local network
    app.run(host='0.0.0.0', port=5001, debug=True)