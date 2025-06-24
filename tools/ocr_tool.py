import streamlit as st
import pytesseract
from PIL import Image
import os

# For Windows: Uncomment and update path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def run_ocr():
    st.subheader("🖼️ Image-to-Text OCR Tool")
    st.write("Upload an image and extract text from it using Tesseract OCR.")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("🧠 Extract Text"):
            with st.spinner("Reading text from image..."):
                text = pytesseract.image_to_string(image)
                st.success("✅ Text extracted successfully!")
                st.text_area("📄 Extracted Text", text, height=250)

                if st.download_button("💾 Download Text", text, file_name="extracted_text.txt"):
                    st.toast("Text downloaded!", icon="✅")
