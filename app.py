import streamlit as st

# Import your tool modules
from tools.ocr_tool import run_ocr
from tools.pdf_summarizer import run_pdf_summarizer
from tools.voice_todo import run_voice_todo

st.set_page_config(page_title="NeuroDesk - AI Toolkit", layout="wide")
st.title("🧠 NeuroDesk - Your AI Productivity Toolkit")

# Sidebar navigation
tool = st.sidebar.selectbox("Choose a tool", [
    "🖼️ Image-to-Text (OCR)",
    "📄 PDF Summarizer",
    "🗣️ Voice To-Do App"
])

# Conditional rendering
if tool == "🖼️ Image-to-Text (OCR)":
    run_ocr()

elif tool == "📄 PDF Summarizer":
    run_pdf_summarizer()

elif tool == "🗣️ Voice To-Do App":
    run_voice_todo()

