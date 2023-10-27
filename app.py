import streamlit as st
import joblib

# Load your trained model
with open('your_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)
vectorizer = joblib.load('vectorizer.pkl')
# Create a Streamlit web app
st.title('Ticket Classification App')
st.write('Enter the ticket description and click the "Predict" button.')

# Input field for ticket description
ticket_description = st.text_input('Ticket Description')

if st.button('Predict'):
    if ticket_description:
        statement=vectorizer.transform(ticket_description)
        predicted_class = model.predict(statement)[0]

        st.write(f'Predicted Class: {predicted_class}')
    else:
        st.warning('Please enter a ticket description.')

