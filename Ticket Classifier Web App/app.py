from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model here
# Example:
model = joblib.load('model/your_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        ticket_text = request.form['ticket_text']

        # Use your model to classify the ticket here
        # Example:
        prediction = model.predict([ticket_text])[0]

        # Return the prediction as JSON
        return jsonify({'prediction': 'Sample Classification'})  # Replace with your actual prediction

if __name__ == '__main__':
    app.run(debug=True)
