import streamlit as st

# ✅ MUST BE FIRST Streamlit command
st.set_page_config(
    page_title="Multimodal AT Agent",
    page_icon="🤖",
    layout="wide"
)

# === Imports ===
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

# === Configure Gemini API ===
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# === Page content ===
st.title("Phidata Multimodal AI Agent - Video Summarizer")
st.header("Powered by Gemini 2.0 Flash Exp")

# === Initialize Agent ===
@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

multimodal_Agent = initialize_agent()

# === File uploader ===
video_file = st.file_uploader(
    "Upload a Video File", 
    type=['mp4', 'mov', 'avi'], 
    help="Upload a video for AI analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI agent will analyze and gather additional details.",
        help="Provide specific questions or insights you want from the video."
    )

    if st.button("Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Upload video to Gemini
                    processed_video = upload_file(video_path)
                    while processed_video.state.name == 'PROCESSING':
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    # Construct the prompt
                    analysis_prompt = f"""
                    Analyze the video for its content and context.
                    Respond to the following query using video insight and supplementary web research:  
                    {user_query}  
                    Provide a detailed, user-friendly, and actionable response.
                    """

                    # Run the AI agent
                    response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                # Display result
                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("Upload a video file to begin analysis.")

# === Style the text area ===
st.markdown(
    """
    <style> 
    .stTextArea textarea {
        height: 100px
    }
    </style>
    """,
    unsafe_allow_html=True
)
