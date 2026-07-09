import streamlit as st # type: ignore

def show_dashboard(game):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("## 🎒 Inventory")

        if game.inventory:
            for item in game.inventory:
                st.success(item)
        else:
            st.info("Inventory Empty")

    with col2:
        st.markdown("## 📖 Journal")

        for note in game.journal:
            st.markdown(f"- {note}")

    with col3:
        st.markdown("## 🎯 Objectives")

        for obj in game.objectives:
            st.markdown(f"⬜ {obj}")