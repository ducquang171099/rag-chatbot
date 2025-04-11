import streamlit as st
from handler import chatbot_response  # import your function

st.set_page_config(page_title="Banking AI Chatbot", page_icon="💬")
st.title("💬 Banking Credit Chatbot")

# Store chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask me anything about credit cards...")

# On new user message
if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = chatbot_response(user_input)
            except Exception as e:
                answer = "⚠️ Error: " + str(e)

            st.markdown(answer)

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": answer})
