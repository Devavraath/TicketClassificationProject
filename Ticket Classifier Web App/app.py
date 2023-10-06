from flask import Flask, render_template, request, jsonify
import joblib
import pickle

app = Flask(__name__)

# Load your model and vectorizer
model = joblib.load('model/your_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        ticket_text = request.form['ticket_text']

        # Preprocess the input text using the loaded vectorizer
        # You may need to adapt this preprocessing to match how the data was preprocessed during training
        ticket_text = vectorizer.transform([ticket_text])  # Reshape to 2D array

        # Make predictions using your model
        prediction = model.predict(ticket_text)[0]

        # Return the prediction as JSON
        return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
