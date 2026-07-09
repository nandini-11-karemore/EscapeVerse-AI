import streamlit as st # type: ignore
from PIL import Image
import os
def show_room(game):
    st.markdown('<div class="game-card">', unsafe_allow_html=True)

    st.subheader(f"🏰 {game.location}")

    image_path = "assets/images/room.jpg"

    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_container_width=True)

    st.caption("The room feels strangely peaceful...")

    st.markdown("### 👀 Visible Objects")

    for obj in game.visible_objects:
        st.write(obj)

    st.markdown("</div>", unsafe_allow_html=True)