import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = "You are a Youtube video summarizer. you will be taking the transcript text and summarizing the entire video in detalis and up to the point and providing the important summary in paragraph within 250 words. PLease provide the summary of the text given here : "
 

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript +=  " " + i['text']
        return transcript
    
    except Exception as e:
        st.error("Error: " + str(e))
        return None
def generate_gemini_content(transcript_text,prompt):

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title = ("Youtube Transcript Summarizer")
youtube_link = st.text_input("Enter the youtube video URL")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Summarize"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('**Summary:**')
        st.write(summary)


