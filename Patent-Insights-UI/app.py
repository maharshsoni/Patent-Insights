import streamlit as st

def process_input(task, user_input):
    # Dummy responses based on the task.
    responses = {
        "Patent Novelty Assessment": f"Assessing novelty for: {user_input}",
        "Patent Claim Generation": f"Generating claim for: {user_input}",
        "Patent Classification": f"Classifying patent: {user_input}",
        "Patent Abstract Generation": f"Generating abstract for: {user_input}",
    }
    return responses[task]

# Main Streamlit UI layout
def main():
    st.title("AI Patent Examiner")

    role = st.radio("Are you a patent examiner or a patent inventor?", ("Patent Examiner", "Inventor"))

    task = None
    if role == "Patent Examiner":
        st.header("Dear Patent Examiner, how can I assist you today?")
        task = st.selectbox("Choose a task:", ["Patent Novelty Assessment", "Patent CPC Classification"])
    elif role == "Inventor":
        st.header("Dear Patent Inventor, how can I assist you today?")
        task = st.selectbox("Choose a task:", ["Patent Claim Generation", "Patent Abstract Generation"])

    if task:
        st.header("Chat with AI")
        user_input = st.text_area("Please enter your input:", key="user_input")

        if st.button("Submit"):
            # Assuming 'process_input' is a function that sends the user's message to the AI and gets a response
            output = process_input(task, user_input)
            
            # Update the conversation in session state
            if 'conversation' not in st.session_state:
                st.session_state.conversation = []
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("AI", output))

            # Clear the text area
            st.session_state.user_input = ""
        
        # Display the conversation
        for author, message in reversed(st.session_state.get('conversation', [])):
            st.text_area(f"{author} says:", value=message, height=75, key=f"msg_{author}_{message}")

if __name__ == "__main__":
    main()
