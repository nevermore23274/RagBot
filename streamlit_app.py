import streamlit as st
import requests

# Streamlit title
st.title('Question Answering with the Apollo Model')

# Streamlit interface for question-answering
st.subheader('Ask a question about the Apollo spacecraft')

question = st.text_input('Enter your question:')
if question:
    # Assuming the model server is running and accessible at 127.0.0.1:8000
    OLLAMA_HOST = 'http://127.0.0.1:8000'  # Replace with the actual host and port
    
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/query", 
            json={"question": question}
        )
        
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer found.")
        else:
            answer = f"Failed to retrieve an answer. Status code: {response.status_code}"

        st.write('Answer:', answer)
    except Exception as e:
        st.write(f"An error occurred: {e}")
