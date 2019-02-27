# @author: Prabhakar Gadupudi
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
sentense = "I bought mobile from ABS website and their service was very bad"
print ne_chunk(pos_tag(word_tokenize(sentense)))