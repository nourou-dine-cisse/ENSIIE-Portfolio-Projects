# Run: streamlit run app.py

import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering
import torch

# CONFIG
st.set_page_config(
    page_title="Visual Question Answering",
    page_icon="🔍",
    layout="centered"
)

# LOAD MODEL (cached — loads once)
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
    model     = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
    model.eval()
    return processor, model

processor, model = load_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model  = model.to(device)

# UI
st.title("MECHENG 4AI3 Project: 🔍 Visual Question Answering")
st.write("Upload an image and ask a question about it.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
question      = st.text_input("Ask a question about the image")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, use_container_width=True)
    if question:
        with st.spinner("Thinking..."):
            inputs  = processor(image, question, return_tensors="pt").to(device)
            with torch.no_grad():
                output  = model.generate(**inputs)
            answer  = processor.decode(output[0], skip_special_tokens=True)

        st.success(f"**Answer: {answer}**")