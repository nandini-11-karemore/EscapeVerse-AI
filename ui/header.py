import streamlit as st  # type: ignore

def show_header():

    st.markdown(
        """
        <div class="title">
            🗝 EscapeVerse AI
        </div>

        <div class="subtitle">
            Infinite AI Escape Adventures
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="status-bar">

        🏰 Laboratory &nbsp;&nbsp;&nbsp;&nbsp;

        ❤️ Health: 100 &nbsp;&nbsp;&nbsp;&nbsp;

        ⭐ Score: 0 &nbsp;&nbsp;&nbsp;&nbsp;

        ⏱ Time: 00:00

        </div>
        """,
        unsafe_allow_html=True
    )