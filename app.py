#Simple Q&A application
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv() #to take all the required variables from the .env
import streamlit as st
import os
from langchain import HuggingFaceHub

def get_openai_response(question):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "XXXXXXXX"
    llm_flan_large = HuggingFaceHub(repo_id = "google/flan-t5-large", model_kwargs = {"temperature" : "0.6", "max_length" : "100"})
    response = llm_flan_large(question)


#Creating the application
st.set_page_config(page_title = "Q&A Demo") #Page title
st.header("LangChain Application")

#getting the input
input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

#submit button
submit = st.button("What is the question")
if submit:
    st.subheader("The Answer is")
    st.write(response)


