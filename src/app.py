import streamlit as st
from typing import Dict, Generator

from PIL import Image
from ollama import Client
from ui.configs import settings

client = Client(host=f'http://{settings.ollama_host}')


def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = client.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


st.set_page_config(page_title="Llama3 assistant")
st.title("Llama 3 assistant")

img = Image.open('assets/akash.png')
st.image(img, width=200)
st.markdown(
    "###### Made with :heart: by [@cro7nis](https://twitter.com/cro7nis)",
    unsafe_allow_html=True)

st.write(
    "The code is open source and available "
    "[here](https://github.com/cro7nis/llama3-assistant) on GitHub. "
    "Special thanks to Meta for releasing [Llama 3](https://ai.meta.com/blog/meta-llama-3/) "
    "and [Ollama](https://ollama.com/) for making it easy to deploy :grin:. The assistant uses the 8B-parameter "
    "model which is fast and requires ~5GB VRAM and it can even run on CPU with reasonable speed. "
    "Input questions below to start chatting!"
)

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "llama3:latest"
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("How could I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            st.session_state.selected_model, st.session_state.messages))
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
