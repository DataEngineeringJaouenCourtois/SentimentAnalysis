from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import re
import numpy as np
nltk.download('punkt')
nltk.download('wordnet')

POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"

def test_text(text, model, tokenizer):
    if text == '':
        return 'no text input'
    clean = clean_sentences_from_text(text)
    clean = tokenizer.texts_to_sequences(clean)
    clean = sequence.pad_sequences(clean , maxlen=48)
    sentiment =  model.predict([clean])[0]
    return decode_sentiment(np.argmax(sentiment))  # Returning a POS/NEG/NEUT

def decode_sentiment(score):
    if score == 1:
        return NEUTRAL
    elif score == 0:
        return NEGATIVE
    else:
        return POSITIVE

def clean_sentences_from_text(text):
    review_text = BeautifulSoup(text).get_text()
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    words = word_tokenize(review_text.lower())
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(i) for i in words]
    return lemma_words