# @author : Prabhakar Gadupudi
from nltk.corpus import wordnet 

# Get anonyms
antonyms = []
word = raw_input("Enter word to generate anonyms (eg: demo) :")
for syn in wordnet.synsets(str(word)):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(str(l.antonyms()[0].name()))
print(antonyms)
print ("="*50)
print(list(set(antonyms)))
print ("="*50)