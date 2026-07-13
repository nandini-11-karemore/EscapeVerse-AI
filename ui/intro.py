import streamlit as st # type: ignore

def show_intro():

    st.markdown("""
    <div style="
        text-align:center;
        padding-top:80px;
        padding-bottom:40px;
    ">
        <h1 style="
            font-size:70px;
            color:gold;
        ">
            🗝 EscapeVerse AI
        </h1>

        <h3 style="
            color:#bbbbbb;
            font-weight:400;
        ">
            Every Room Tells A Story
        </h3>
    </div>
    """, unsafe_allow_html=True)

    return st.button(
        "▶ Begin Adventure",
        use_container_width=True
    )