import re

def most_common_word(text):
    stopwords = {"is", "a", "the", "of", "and", "to", "in", "on", "at", "for", "with", "as", "by", "an", "this", "that", "it", "be"}
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = {} 
    for i in words:
        if i not in stopwords: 
            word_counts[i] = word_counts.get(i, 0) + 1 

    most_common = max(word_counts, key=word_counts.get) if word_counts else None

    return most_common, word_counts[most_common] if most_common else 0

text = "This is a test. This test is only a test."
i, count = most_common_word(text)
print(f"The most common word is '{i}' which appears {count} times.")
