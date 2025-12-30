import streamlit as st
import uuid
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

# -------------------- UTILITIES --------------------

def generate_uuid():
    return str(uuid.uuid4())

def add_thread(thread_id):
    if thread_id not in st.session_state.chat_threads:
        st.session_state.chat_threads.append(thread_id)

def reset_chat():
    new_thread_id = generate_uuid()
    st.session_state.thread_id = new_thread_id
    add_thread(new_thread_id)
    st.session_state.message_history = []
def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable':{'thread_id':thread_id}}).values['messages']

# -------------------- SESSION STATE INIT --------------------

if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_uuid()

if "chat_threads" not in st.session_state:
    st.session_state.chat_threads = []

if "message_history" not in st.session_state:
    st.session_state.message_history = []

add_thread(st.session_state.thread_id)

# -------------------- SIDEBAR UI --------------------

st.sidebar.title("AI Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")
for thread_id in st.session_state.chat_threads[::-1]:
    if st.sidebar.button(thread_id):
        st.session_state['thread_id']= thread_id
        messages=load_conversation(st.session_state.thread_id)
        temp_messages=[]
        for message in messages:
            if isinstance(message,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role':role,'content':message.content})
        st.session_state['message_history']=temp_messages
        
        
        

# -------------------- CONFIG --------------------

CONFIG = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

# -------------------- LOAD CHAT HISTORY --------------------

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- CHAT INPUT --------------------

user_input = st.chat_input("Type your message here...")

if user_input:
    # USER MESSAGE
    st.session_state.message_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ASSISTANT MESSAGE (STREAMING)
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
            if message_chunk.content
        )

    # SAVE AI RESPONSE
    st.session_state.message_history.append({
        "role": "assistant",
        "content": ai_message
    })
