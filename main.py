import streamlit as st



st.title('Hello anjali')
st.write('This is a simple Streamlit app.')

if st.button('hello Streamlit app.'):
    st.text('Hello, Streamlit!')

name = st.text_input('Please enter your name:')
if name:
    st.write(f'Hello, {name}!')

file = st.file_uploader('Please upload a file:', type=['txt', 'csv'])
if file:
    st.write('Thanks for uploading a file!')
