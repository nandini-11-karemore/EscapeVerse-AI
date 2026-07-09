import streamlit as st  # type: ignore[import]

def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"]{
        font-family: 'Inter', sans-serif;
    }

    .stApp{
        background:#0B0F19;
        color:white;
    }

    #MainMenu,
    footer,
    header{
        visibility:hidden;
    }

    .title{
        font-family:'Cinzel',serif;
        font-size:48px;
        color:#D4AF37;
        text-align:center;
        font-weight:700;
        margin-bottom:5px;
    }

    .subtitle{
        text-align:center;
        color:#9CA3AF;
        margin-bottom:30px;
        font-size:18px;
    }

    .game-card{

        background:#171E2D;

        border:1px solid #2A3448;

        border-radius:18px;

        padding:20px;

        margin-bottom:18px;

        box-shadow:0 0 15px rgba(0,0,0,.25);

    }

    h2,h3{
        color:#D4AF37;
    }

    .status-bar{

        background:#111827;

        border-radius:15px;

        padding:15px;

        border:1px solid #2A3448;

        margin-bottom:20px;

    }

    </style>
    """, unsafe_allow_html=True)