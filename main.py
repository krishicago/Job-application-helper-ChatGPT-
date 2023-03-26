import streamlit as st
import pandas as pd
from io import StringIO
import PyPDF2

import os
import openai

openai.api_key = "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"


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")
    

    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    pdfreader=PyPDF2.PdfReader(uploaded_file.name)
    # (bytes_data)
    
    #This will store the number of pages of this pdf file
    x= len(pdfreader.pages)

    print(x)
    
    #create a variable that will select the selected number of pages
    pageobj= pdfreader.pages[x-1]
    
    #(x+1) because python indentation starts with 0.
    #create text variable which will store all text datafrom pdf file
    text=pageobj.extract_text()

    # st.write(text)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Find education details of following resume\n\n{text}",
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )

    st.title("Educational Summary")
    st.write(response["choices"][0]["text"])



    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate positional statement of the following resume as first person\n\n{text}",
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )


    st.title("Positional Statement")
    st.write(response["choices"][0]["text"])


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a cover letter of the following resume\n\n{text}",
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )

    st.title("Cover letter")

    st.write(response["choices"][0]["text"])


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract skills from this resume:\n\n{text}",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )

    st.title("Keyword")

    st.write(response["choices"][0]["text"])
