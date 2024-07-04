import streamlit as st

from qa_bot import qa_bot

# https://chatgpt.com/share/53192091-232a-491d-9cd3-aa510390dc1a

# Streamlit UI
st.title("AMA Bot")

# Input box for user query
user_query = st.text_input("Enter your question:")

# Button to invoke the function
if st.button("Ask me"):
    with st.spinner('Processing...'):
        result = qa_bot(user_query)
        st.success("Done!")
        # Output for showing the results
        st.write(result)   