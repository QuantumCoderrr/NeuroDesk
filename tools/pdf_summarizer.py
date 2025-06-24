import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

# Load summarizer once
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

def run_pdf_summarizer():
    st.subheader("📄 PDF Summarizer")
    st.write("Upload a PDF and get an AI-generated summary.")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        with st.spinner("Reading PDF..."):
            pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = ""
            for page in pdf_doc:
                text += page.get_text()
        
        if len(text.strip()) == 0:
            st.error("❌ Could not extract any text from the PDF.")
            return

        st.success("✅ Extracted text from PDF.")
        st.text_area("📄 Full Text", text[:3000], height=250, help="Showing first 3000 characters.")

        if st.button("🧠 Summarize"):
            with st.spinner("Generating summary..."):
                # BART handles ~1024 tokens max, so truncate if needed
                if len(text) > 3000:
                    text = text[:3000]
                summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                st.success("✅ Summary generated!")
                st.text_area("📝 Summary", summary, height=200)

                if st.download_button("💾 Download Summary", summary, file_name="summary.txt"):
                    st.toast("Summary downloaded!", icon="✅")
