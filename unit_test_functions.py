import unittest
from docker_app.web_app.src.model import *
from keras.models import load_model
import pickle

model = load_model('docker_app/web_app/models/SentimentAnalysis.h5')
with open('docker_app/web_app/models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

class TestModel(unittest.TestCase):
    def testing_test_text(self):
        self.assertEqual(test_text('goose',model,tokenizer),'NEUTRAL')
        self.assertEqual(test_text('bad',model,tokenizer),'NEGATIVE')
        self.assertEqual(test_text('good',model,tokenizer),'POSITIVE')
        self.assertEqual(test_text('',model,tokenizer),'no text input')

    def testing_clean_sentences_from_text(self):
        self.assertEqual(clean_sentences_from_text('WHAT A GOOSE'),['what', 'a', 'goose'])
        self.assertEqual(clean_sentences_from_text('WHAT a ^GOOSE'),['what', 'a', 'goose'])
        self.assertEqual(clean_sentences_from_text('WhAt a  ^GOoSE'), ['what', 'a', 'goose'])
        self.assertEqual(clean_sentences_from_text('        WhAt a  %GOoSE'), ['what', 'a', 'goose'])
        self.assertEqual(clean_sentences_from_text('        WhAt a  %GOoSE !'), ['what', 'a', 'goose'])

    def testing_decode_sentiment(self):
        self.assertEqual(decode_sentiment(0),'NEGATIVE')
        self.assertEqual(decode_sentiment(1),'NEUTRAL')
        self.assertEqual(decode_sentiment(2),'POSITIVE')

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)