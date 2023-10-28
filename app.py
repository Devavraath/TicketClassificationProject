import streamlit as st
import joblib

# Load your trained model
model = joblib.load('your_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Create a Streamlit web app
st.title('Ticket Classification App')
st.write('Enter the ticket description and click the "Predict" button.\n')
st.image('Categories.jpeg', width=300)
')

# Input field for ticket description
ticket_description = st.text_input('Ticket Description')

if st.button('Predict'):
    if ticket_description:
        # Preprocess the input using the vectorizer
        statement = vectorizer.transform([ticket_description])

        # Use your model to make predictions
        predicted_class = model.predict(statement)[0]

        st.write(f'Predicted Class: {predicted_class}')
    else:
        st.warning('Please enter a ticket description.')
