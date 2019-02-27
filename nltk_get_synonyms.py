# @author : Prabhakar Gadupudi
from nltk.corpus import wordnet 

synonyms = []
word = raw_input("Enter keyword for generating synonyms (eg: Demo) :")
for syn in wordnet.synsets(str(word)):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print ("="*50)
print(list(set(synonyms)))
print ("="*50)