import re
from nltk import word_tokenize, pos_tag
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def simplify_text(text):
    import re
    text = re.sub(r"වසර\s*(\d+)", r"\1දී", text)
    return text.replace("ස්ථාවර තත්ත්වයකට පත්වෙයි", "සෙරිනවට පත්වෙයි")

def pos_analysis(text):
    # Just split into words – skip advanced tokenizing
    words = text.split()
    return [(word, "UNK") for word in words]
