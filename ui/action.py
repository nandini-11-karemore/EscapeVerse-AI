import streamlit as st # type: ignore

def show_action():

    st.markdown("""
    <div class="game-card">
        <h3>⚡ What will you do?</h3>
    """, unsafe_allow_html=True)

    action = st.text_input(
        "",
        placeholder="inspect computer, read journal, open drawer..."
    )

    submit = st.button("⚡ Perform Action", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    return action, submit