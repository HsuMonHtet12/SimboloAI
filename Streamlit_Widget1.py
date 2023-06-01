import streamlit as st

name = st.text_input('Enter your name')
course = st.selectbox(
    'Choose the course',
    ('AI', 'Python Programming','React.js'))

classType = st.radio(
    "Choose the class type",
    ('Online', 'Offline'))

click=st.button('Done')
st.write(click)
if click:
    st.write('Hello, My Name is ', name, '...')
    st.write('I am learning ', course, 'which is an ',classType,' class at Simbolo.')

