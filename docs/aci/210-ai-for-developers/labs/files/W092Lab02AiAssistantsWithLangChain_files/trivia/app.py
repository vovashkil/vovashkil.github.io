############################################## Chains ############################################

from chains import report_writer, promotion_maker, trivia_simulator, buffer_chat, window_chat, summary_chat, dynamodb_chat, delete_table, create_dynamo_chat

################################################ UI ##############################################

###########  Decoration  ###########

import streamlit as st

# Set the title of the app
st.set_page_config(page_title="Trivia Assistant")

# Add a title to the app
st.title("Welcome to the Ultimate Trivia Assistant")

with st.sidebar:
     st.logo("./images/bedrock_langchain.png")

st.sidebar.write("# Tools")

###########  Tool selection  ###########

if "tool" not in st.session_state:
    st.session_state.tool = 'none'

if st.sidebar.button('Promotion Maker'):
    st.session_state.tool = 'promotion'
if st.sidebar.button('Report Writer'):
    st.session_state.tool = 'report'
if st.sidebar.button('Trivia Simulator'):
    st.session_state.tool = 'simulator'
if st.sidebar.button('Chat'):
    st.session_state.tool = 'chat'
if st.session_state.tool == 'none':
    st.write('Select a tool from the sidebar')

###########  Report writer  ###########

elif st.session_state.tool == "report":

    subject = st.text_input(
        "Report subject 👇",
        placeholder = "The Empire State Building"
    )
    if subject:
        st.write(report_writer(subject))

###########  Promotion maker  ###########

elif st.session_state.tool == "promotion":
    theme = st.text_input(
        "Theme 👇",
        placeholder = "Football"
    )
    time_of = st.text_input(
        "Time 👇",
        placeholder = "February 8th, 7pm EST"
    )
    location = st.text_input(
        "Location 👇",
        placeholder = "New York Pub"
    )

    button = st.button('Submit')

    if button:
        st.write(promotion_maker(theme, time_of, location))

###########  Trivia simulator  ###########

elif st.session_state.tool == "simulator":
    topic = st.text_input(
        "Topic 👇",
        placeholder = "Dog breeds"
    )
    if topic:
        responses = trivia_simulator(topic)
        st.subheader("Question", divider=True)
        st.write(responses[0])
        st.subheader("Marissa's response", divider=True)
        st.write(responses[1])
        st.subheader("Diego's response", divider=True)
        st.write(responses[2])
        st.subheader("Host Ruling", divider=True)
        st.write(responses[3])

###########  chatbots  ###########

elif st.session_state.tool == "chat":
    if "messages" not in st.session_state:
        st.session_state.messages = []

    ####  Streamlit message management  ####

    def add_message(memory_type, prompt):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                        st.markdown(prompt)
            with st.chat_message("assistant"):
                        if memory_type == "buffer":
                            response = buffer_chat(prompt)
                        elif memory_type == "window":
                            response = window_chat(prompt)
                        elif memory_type == "summary":
                            response = summary_chat(prompt)
                        elif memory_type == "dynamodb":
                            response = dynamodb_chat(prompt)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})

    memory_type = st.sidebar.radio(label = "Memory type", options = ['buffer','window','summary','dynamodb'], index = 0)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    ####  Chatbot memory options  ####

    if memory_type == "buffer":
        st.session_state.messages = []
        if prompt := st.chat_input("Let's talk trivia"):
            add_message(memory_type, prompt)
    elif memory_type == "window":
        st.session_state.messages = []
        if prompt := st.chat_input("Let's talk trivia"):
             add_message(memory_type, prompt)
    elif memory_type == "summary":
        st.session_state.messages = []
        if prompt := st.chat_input("Let's talk trivia"):
            add_message(memory_type, prompt)
    elif memory_type == "dynamodb":
        st.session_state.messages = []
        if st.sidebar.button('Create Table'):
            create_dynamo_chat()
            st.sidebar.write("Table Created")
        if st.sidebar.button('Delete Table'):
            delete_table()
            st.session_state.messages = []
            st.sidebar.write("Table Deleted")
        if prompt := st.chat_input("Let's talk trivia"):
            add_message(memory_type, prompt)
 