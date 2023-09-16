import streamlit as st
import openai

st.title("Tavacode - Intergrate Chat GPT using Python")

# Setup model
model = "text-davinci-003"

with open("apikey.txt", "r") as f:
    openai.api_key = f.readline()

def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine = model,
        prompt = user_question,
        max_token = 1024,
        n = 1,
        temperate = 0.5
    )

    response_text = response.choices[0].text
    return response_text


def main():
    user_question = st.text_input("Nhap cau hoi vao day")
    if st.button("Chat voi em di"):
        response_text = get_response_from_chatgpt(user_question)
        return st.write(f"{user_question} {response_text}")
    
main()

