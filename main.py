# This is a streamlit website
import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
import requests
import os
from data import teams

load_dotenv()


def get_player_meaning(team, jersey_number, position, country):
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    # url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    model = genai.GenerativeModel("gemini-2.0-flash")
    payload =  f"guuess famous guy from {team}, {jersey_number},  {country}, if not found in {teams}, then use your knowledge or google it"
    
    try:
        response = model.generate_content(payload)
        response_data = response.text
        return response_data #["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error fetching data: {str(e)}"


def main():
    columns = st.columns(2)
    
    with columns[0]:
        st.title("Welcome to Arunan's Place.\n### Here we guess soccer players' name.")
        st.header("No... i'm not a soccer player, i'm just a kiddo.")
    with columns[1]:
        st.image("image.png")

    st.title("Soccer Player Guessing Game")

    team = st.text_input("Enter the team name:")
    jersey_number = st.number_input("Enter the jersey number:", min_value=1, max_value=99, step=1)
    
    position = st.text_input("Enter the player's position:")
    country = st.text_input("Enter the player's country:")

    guess = ""
    
    if st.button("Get Player Meaning!"):
        meaning = get_player_meaning(team, jersey_number, position, country)
        st.write(meaning)



 

if __name__ == "__main__":
    main()

