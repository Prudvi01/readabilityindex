import re
import string

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def sentence_count(text):
    sentences_list = (re.split(r'[.!?]+', text))
    while("" in sentences_list) : 
        sentences_list.remove("") 
    sentences = len(sentences_list)
    return sentences

def word_count(text):
    return sum([i.strip(string.punctuation).isalpha() for i in text.split()])