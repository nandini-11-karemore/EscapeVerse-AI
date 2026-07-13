import streamlit as st # type: ignore
import os
from PIL import Image, UnidentifiedImageError

def show_room(game):

    st.markdown("<div class='game-card'>", unsafe_allow_html=True)

    st.subheader(f"🏰 {game.current_location}")

    location = game.current_location.lower().replace(" ", "")

    # ---------- IMAGE ----------
    image_path = f"assets/generated/{location}.jpg"

    try:
        image = Image.open(image_path)

    except (FileNotFoundError, UnidentifiedImageError):

       image = Image.open("assets/images/room.jpg")

    st.image(image, use_container_width=True)

    # ---------- SOUND ----------
    sound_path = f"assets/sounds/{location}.mp3"

    if os.path.exists(sound_path):
        with open(sound_path, "rb") as audio:
            st.audio(audio.read())

    # ---------- OBJECTS ----------
    st.markdown("### 👀 Visible Objects")

    clicked = None

    cols = st.columns(2)

    for i, obj in enumerate(game.visible_objects):

        with cols[i % 2]:

            if st.button(obj, use_container_width=True):
                clicked = f"inspect {obj}"

    st.markdown("</div>", unsafe_allow_html=True)

    return clicked