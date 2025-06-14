# 📖 SinhalaReadAid – Assistive Reading Tool

A free and open-source **Sinhala NLP-based assistive reading tool** designed to support Sinhala speakers, students, and individuals with reading difficulties. Built with `Python`, `Streamlit`, and `PyTorch`, it simplifies complex Sinhala text, generates text-to-speech audio, and visualizes linguistic patterns to aid understanding.

🔗 **Live App:**  
👉 [https://sinhalareadaid-3qnc5mv5xs7qhg7pzcbzfw.streamlit.app/](https://sinhalareadaid-3qnc5mv5xs7qhg7pzcbzfw.streamlit.app/)

---

## 🎯 Features

- ✍️ **Sinhala Text Input**  
  Paste or type any Sinhala sentence for real-time processing.

- 🔁 **Text Simplification**  
  Rewrites complex text into simpler forms using rule-based logic.

- 🔈 **Text-to-Speech (TTS)**  
  Generates clear Sinhala speech using `gTTS` (Google Text-to-Speech).

- 📊 **Word Frequency Visualization**  
  Bar chart showing most frequent words using `matplotlib`.

- 🧠 **POS Tagging**  
  Basic part-of-speech tagging (with placeholders for Sinhala support).

---

## 🧪 Technologies Used

| Tool/Library     | Purpose                                |
|------------------|----------------------------------------|
| Python           | Core programming language              |
| Streamlit        | Interactive web UI                     |
| gTTS             | Sinhala Text-to-Speech                 |
| Matplotlib       | Data visualization (word frequency)    |
| NLTK             | Text tokenization, POS tagging basics  |
| PyTorch (optional)| NLP model integration (future upgrade)|

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash```
git clone https://github.com/yourusername/SinhalaReadAid.git
cd SinhalaReadAid

---

2. **Install dependencies**

```bash```
pip install -r requirements.txt

---

3. **Run the app locally**

```bash```
streamlit run app.py
