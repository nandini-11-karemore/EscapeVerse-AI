import streamlit as st # type: ignore
from ui.typewriter import typewriter

def show_story(game):
    typewriter(game.story)
    with st.spinner("The world is changing..."):
        pass

    with st.container():
        st.markdown("## 📖 Story")

        st.markdown(
            f"""
            <div style="
                background:#171E2D;
                border:1px solid #2A3448;
                border-radius:15px;
                padding:20px;
                font-size:18px;
                line-height:1.8;
                color:white;
            ">
            {game.story.replace(chr(10), "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )