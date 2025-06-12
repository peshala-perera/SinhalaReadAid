import re
from nltk import word_tokenize, pos_tag
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def simplify_text(text):
    text = re.sub(r"වසර\s*(\d+)", r"\1දී", text)
    return text.replace("ස්ථාවර තත්ත්වයකට පත්වෙයි", "සෙරිනවට පත්වෙයි")

def pos_analysis(text):
    words = word_tokenize(text)
    return pos_tag(words)
