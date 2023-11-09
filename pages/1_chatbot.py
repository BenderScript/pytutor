import openai
import streamlit as st

from text_docs_processor import TextDocProcessor

st.set_page_config(page_title="GenAI Transcriber", page_icon=":rocket:", layout="wide")
st.title("ChatBot")

# Initialize KoshaTextDocs
if 'text_doc_processor' not in st.session_state:
    # TODO navigate to stop
    st.session_state.text_doc_processor = TextDocProcessor()

text_doc_processor = st.session_state.text_doc_processor

if st.session_state.chatbot_created:
    if prompt := st.chat_input("AMA!", key="chat_input"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            prompt_placeholder = st.empty()
            prompt_placeholder.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        try:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                conv_chain_full_response = text_doc_processor.text_conv_chain({"question": prompt})
                message_placeholder.markdown(conv_chain_full_response["answer"] + "▌")
                st.session_state.messages.append({"role": "assistant", "content": conv_chain_full_response["answer"]})
        except openai.error.RateLimitError as e:
            st.error("OpenAI API rate limit exceeded. Please try again later.")

else:
    st.error("Chatbot not created yet. Ingest data first.")
