from flask import Flask, request, render_template
import pickle
import joblib

app = Flask(__name)
vectorizer = joblib.load('vectorizer.pkl')
# Load your trained model
with open('your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def classify_ticket():
    predicted_class = None

    if request.method == 'POST':
        ticket_description = request.form['ticket_description']
        
        statement = vectorizer.transform(ticket_description)

        # Use your model to make predictions
        predicted_class = model.predict(statement)[0]

    return render_template('index.html', predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
