import streamlit as st
import os

# Import always-safe tools
from tools.ocr_tool import run_ocr
from tools.pdf_summarizer import run_pdf_summarizer

# Try importing the voice tool only if running locally
enable_voice = os.getenv("USE_VOICE", "true").lower() == "true"
if enable_voice:
    try:
        from tools.voice_todo import run_voice_todo
        voice_supported = True
    except Exception as e:
        voice_supported = False
        st.sidebar.warning("⚠️ Voice To-Do not available in this environment.")
else:
    voice_supported = False

# Page settings
st.set_page_config(page_title="NeuroDesk - AI Toolkit", layout="wide")
st.title("🧠 NeuroDesk - Your AI Productivity Toolkit")

# Sidebar options
options = [
    "🖼️ Image-to-Text (OCR)",
    "📄 PDF Summarizer"
]
if voice_supported:
    options.append("🗣️ Voice To-Do App")

tool = st.sidebar.selectbox("Choose a tool", options)

# Tool router
if tool == "🖼️ Image-to-Text (OCR)":
    run_ocr()

elif tool == "📄 PDF Summarizer":
    run_pdf_summarizer()

elif tool == "🗣️ Voice To-Do App" and voice_supported:
    run_voice_todo()

