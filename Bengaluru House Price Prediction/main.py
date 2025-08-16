from flask import Flask, render_template, request

app = Flask(__name__)  # Creates a Flask app instance

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Renders the HTML template

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Starts the Flask server on port 5001
