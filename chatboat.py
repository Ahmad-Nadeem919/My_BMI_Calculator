import google.generativeai as genai
import streamlit as st

st.title("My AI Chatboat")

# I have Set my Gemini API key here
genai.configure(api_key="AIzaSyCmU5f3PdXRakfjL8Rul-UGi9Yfbf7rXfM")

# Initialize the model by giving a sepesific name of a model according to apiket
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
st.write("Enter bye for exit")    

user_input = st.text_input("You :")
st.button("enter")


if user_input:
    if user_input.lower() == "bye":
        st.write("Chatbot: Goodbye!")
    else:
        try:
            response = model.generate_content(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Chatbot", response.text))
        except Exception as e:
            st.write("Chatbot: Oops, something went wrong!", e)

# Display chat history
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")
