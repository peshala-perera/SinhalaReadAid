import streamlit as st
from nlp_utils import simplify_text, pos_analysis
from tts_utils import text_to_speech_sinhala
from viz_utils import plot_word_freq

st.set_page_config(page_title="SinhalaReadAid", layout="centered")
st.title("📖 SinhalaReadAid - Assistive Reading Tool")

text_input = st.text_area("✍️ Enter Sinhala Text:", height=150)

if text_input:
    st.subheader("✅ Simplified Text")
    simplified = simplify_text(text_input)
    st.write(simplified)

    st.subheader("🔈 Text-to-Speech")
    audio_path = text_to_speech_sinhala(simplified)
    st.audio(audio_path)

    st.subheader("📊 Word Frequency")
    image_path = plot_word_freq(simplified)
    st.image(image_path)

    st.subheader("🧠 POS Tags")
    pos_tags = pos_analysis(simplified)
    st.table(pos_tags)
