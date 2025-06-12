import matplotlib.pyplot as plt
from collections import Counter
import nltk

def plot_word_freq(text):
    words = nltk.word_tokenize(text)
    counts = Counter(words)
    top_words = counts.most_common(10)

    labels, values = zip(*top_words)

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = "word_freq.png"
    plt.savefig(filename)
    return filename
