import streamlit as st
from gradio import Interface

# Dummy functions to simulate interaction.
# Replace these with your actual model inference functions.
def patent_novelty_assessment(user_input):
    return f"Novelty Assessment result for: {user_input}"

def patent_claim_generation(user_input):
    return f"Generated Claim for: {user_input}"

def patent_classification(user_input):
    return f"Classification result for: {user_input}"

def patent_abstract_generation(user_input):
    return f"Generated Abstract for: {user_input}"

# Streamlit UI
def main():
    st.title("Patent Insights")
    
    # Role selection
    role = None
    if st.button("Patent Examiner"):
        role = "examiner"
    elif st.button("Inventor"):
        role = "inventor"

    # Chat interfaces
    if role == "examiner":
        st.header("Dear Patent Examiner, I am trained to help you with two tasks:")
        if st.button("Patent Novelty Assessment Chat"):
            st.session_state['chat_function'] = patent_novelty_assessment
            st.session_state['chat_title'] = "Patent Novelty Assessment Chat"
        if st.button("Patent CPC Classification Chat"):
            st.session_state['chat_function'] = patent_classification
            st.session_state['chat_title'] = "Patent CPC Classification Chat"

    elif role == "inventor":
        st.header("Dear Patent Inventor, I am trained to help you with two tasks:")
        if st.button("Patent Claim Generation Chat"):
            st.session_state['chat_function'] = patent_claim_generation
            st.session_state['chat_title'] = "Patent Claim Generation Chat"
        if st.button("Patent Abstract Generation Chat"):
            st.session_state['chat_function'] = patent_abstract_generation
            st.session_state['chat_title'] = "Patent Abstract Generation Chat"

    # Display chat interface if any chat_function is set
    if 'chat_function' in st.session_state:
        user_input = st.text_input("Your message", key='user_input')
        if user_input:
            result = st.session_state['chat_function'](user_input)
            st.write(result)
        st.subheader(st.session_state['chat_title'])

    # Style the app using Streamlit's theming if desired

if __name__ == "__main__":
    main()
