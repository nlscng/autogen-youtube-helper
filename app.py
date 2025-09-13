import streamlit as st

st.title('Chat with YouTube Videos')

url = st.text_input('Enter YouTube video URL:')

chat_container = st.container()

prompt = st.chat_input('Ask a question about the video:')

if prompt and url:
    with chat_container:
        st.write(prompt)