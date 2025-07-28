import streamlit as st
from utils.model_loader import load_model

st.set_page_config(page_title="Roadmapper", layout="centered")

st.title("🎯 Roadmapper: Your Personalized Learning Path")
skill = st.text_input("Enter a skill you want to master:")

if skill:
    with st.spinner("Generating roadmap..."):
        model = load_model()
        prompt = f"Create a personalized learning roadmap for mastering {skill}."
        result = model(prompt)
        st.success("Here is your roadmap:")
        st.markdown(result)