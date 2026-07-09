import streamlit as st # type: ignore

from ui.styles import load_css
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
# UI
show_header()

show_room(game)
show_story(game)

action, submit = show_action()

if submit:
    engine.process_action(game, action)
    st.rerun()

show_dashboard(game)