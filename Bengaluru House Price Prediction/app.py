from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Dummy prediction (replace with ML model later)
    predicted_price = sqft * 5000  

    return render_template('index.html', prediction=round(predicted_price, 2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
