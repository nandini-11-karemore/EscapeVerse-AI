import streamlit as st # type: ignore
import time

def typewriter(text, speed=0.02):

    placeholder = st.empty()

    output = ""

    for ch in text:
        output += ch
        placeholder.markdown(output)
        time.sleep(speed)