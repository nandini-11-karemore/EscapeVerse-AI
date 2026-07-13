import streamlit as st # type: ignore

from ui.styles import load_css
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    from ui.intro import show_intro

    if show_intro():
        st.session_state.started = True
        st.rerun()

    st.stop()
from ui.header import show_header
from ui.room import show_room
from ui.story import show_story
from ui.action import show_action
from ui.dashboard import show_dashboard
from engine.game_state import GameState
from engine.game_engine import GameEngine
st.set_page_config(
    page_title="EscapeVerse AI",
    page_icon="🗝",
    layout="wide"
)

load_css()

# Create game state FIRST
if "game" not in st.session_state:
    st.session_state.game = GameState()

game = st.session_state.game
if "engine" not in st.session_state:
    st.session_state.engine = GameEngine()

engine = st.session_state.engine
# 👇 ADD THE SIDEBAR HERE
from engine.save_manager import save_game, load_game

with st.sidebar:

    st.title("🎮 EscapeVerse")

    if st.button("💾 Save Game"):
        save_game(game)
        st.success("Game Saved!")

    if st.button("📂 Load Game"):
        if load_game(game):
            st.success("Game Loaded!")
            st.rerun()

    if st.button("💡 Hint"):
        hint = engine.get_hint(game)
        st.info(hint)

show_header(game)

left, right = st.columns([2, 1])

with left:

    quick_action = show_room(game)

    show_story(game)

with right:

    show_dashboard(game)

action, submit = show_action()

if quick_action:
    with st.spinner("Thinking..."):
        engine.process_action(game, quick_action)
    st.rerun()

if submit and action:
    with st.spinner("Thinking..."):
        engine.process_action(game, action)
    st.rerun()