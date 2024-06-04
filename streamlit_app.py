import streamlit as st
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
import os
import requests

# Concrete implementation of DummyLLM
class ConcreteDummyLLM(LLM):
    def _call(self, prompt: str, stop=None) -> str:
        return "This is a dummy response."
    
    def _llm_type(self) -> str:
        return "dummy"

st.title('Question Answering Bot')

# Dropdown for model selection
st.subheader('Select a model to use with Ollama')
models = ["[choose model]", "gemma:7b"]
selected_model = st.selectbox("Choose a model", models)

# Function to load the actual model
def load_actual_model(model_name):
    class ActualLLM(LLM):
        def _call(self, prompt: str, stop=None) -> str:
            # Send a request to the model
            url = f"http://ollama-container:11434/models/{model_name}/generate"
            headers = {"Content-Type": "application/json"}
            data = {"prompt": prompt}
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                return response.json().get('result', 'No result found')
            else:
                return f"Error: {response.status_code}, {response.text}"
        
        def _llm_type(self) -> str:
            return model_name
    return ActualLLM()

# Button to pull the selected model
if selected_model != "[choose model]" and st.button("Pull Model"):
    try:
        response = requests.post(
            "http://ollama-container:11434/pull_model",
            json={"model_name": selected_model}
        )
        if response.status_code == 200:
            st.success(f"Model '{selected_model}' pulled successfully.")
        else:
            st.error(f"Failed to pull the model. Error: {response.text}")
    except Exception as e:
        st.error(f"Failed to pull the model. Error: {e}")

# Load documents from data/pdfdata directory
data_dir = 'data/pdfdata'
documents = []
for filename in os.listdir(data_dir):
    if filename.endswith('.pdf'):
        loader = PyPDFLoader(os.path.join(data_dir, filename))
        documents.extend(loader.load())

# Initialize LangChain components
embeddings = OllamaEmbeddings(base_url="http://ollama-container:11434")
qdrant = Qdrant.from_documents(documents, embeddings, url="http://qdrant:6333")

# Use the actual LLM if a model is selected, otherwise use ConcreteDummyLLM
if selected_model != "[choose model]":
    actual_llm = load_actual_model(selected_model)
else:
    actual_llm = ConcreteDummyLLM()

# Define the QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=actual_llm,
    chain_type="stuff",
    retriever=qdrant.as_retriever()
)

# Streamlit interface for question-answering
question = st.text_input('Enter your question:')

if question:
    try:
        response = qa_chain.invoke({"query": question})
        st.write('Answer:', response)
    except Exception as e:
        st.write(f"An error occurred: {e}")

