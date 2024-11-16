import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyB4tK6azgrb_-VQSgsNT2BW29ABjwaxJII")

sys_prompt = """ You are helpful AI tutor for Data Science
                Students will ask you doubts related to various topics in data science.
                you are expected to reply in as much as possible.
                make sure to take examples while explaining a concept.                
             """
model = ai.GenerativeModel(model_name='models/gemini-1.5-flash',system_instruction=sys_prompt)



st.title("Data Science Tutor Application")

user_prompt = st.text_area("Enter your query!...", 
             placeholder="Type your query here...")

btn_click = st.button("Generate Answer",type="primary")

# st.write(btn_click)

if btn_click == True:
    # do something
    # generate the answers / responses 
    # we need to gemini or gpt model, configure ( set the api key), call the model to generate responses
    response = model.generate_content(user_prompt)
    st.write(response.text)