import streamlit as st
from chatbot import bot

st.set_page_config(
    page_title="Parth's Data Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for first visit
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Access control
 #   password = st.text_input("Enter password", type="password", value="parth2025")
  #  if password != "parth2025":
   #     st.warning("🔒 Please enter the correct password")
    #    st.stop()
    
    #st.success("✅ Access granted!")
    
    # Show available commands
    with st.expander("📚 View Available Commands"):
        help_result = bot.chat("commands")
        st.markdown(help_result['response'])

# Main interface
st.title("💬 Parth's Data Assistant")

# WELCOME MESSAGE - Show only on first visit
if st.session_state.first_visit:
    st.info("👋 **Welcome!** Type 'commands' to see what I can help you with.")
    st.session_state.first_visit = False

# Display chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "data" in message and message["role"] == "assistant":
            with st.expander("🔍 View Raw Data"):
                st.json(message["data"])

# User input - Always show at bottom
query = st.chat_input("Ask me anything... (type 'commands' for help)")

if query:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(query)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            result = bot.chat(query)
        
        # Display formatted response
        st.markdown(result['response'])
        
        # Show raw data for data intents
        if result['intent'] in ['sales_data', 'customer_count', 'inventory']:
            with st.expander("🔍 View Raw Data"):
                st.json(result['data'])
    
    # Add assistant message to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": result['response'],
        "data": result['data'] if result['intent'] != 'help' else None
    })
    
    # Auto-show commands if user asks for help
    if result['intent'] == 'help':
        st.info("💡 Tip: The command list is also available in the sidebar!")