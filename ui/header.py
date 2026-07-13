import streamlit as st  # type: ignore

def show_header(game):

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
    progress = min(game.score / 100, 1.0)

    st.progress(progress)
    st.markdown(
        """
        <div class="status-bar">

        🏰 {game.current_location}


        ❤️ Health: 100 &nbsp;&nbsp;&nbsp;&nbsp;

        ⭐ Score: {game.score}

        ⏱ Time: 00:00

        </div>
        """,
        unsafe_allow_html=True
    )