import matplotlib.pyplot as plt
from collections import Counter
import nltk

nltk.download('punkt')

def plot_word_freq(text):
    # Direct word split — avoid sentence tokenizer entirely
    words = text.split()
    counts = Counter(words)
    top_words = counts.most_common(10)

    if not top_words:
        return None

    labels, values = zip(*top_words)

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = "word_freq.png"
    plt.savefig(filename)
    return filename
