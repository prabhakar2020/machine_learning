# @author: Prabhakar Gadupudi
#Polarity : It simply means emotions expressed in a sentence. It evaluate emotions (Rational emotions)
#Subjectivity : Subjective sentence expresses some personal feelings, views, or beliefs.
# < 0 result will be negative 
# > 0 results indicates percentage of positive. Usually expected > 60 for good positie result
from textblob import TextBlob
statement = "I went to hotel today. smell was good but taste was not good"

sentiment = TextBlob(statement)
print("Sentiment Score: ", sentiment.sentiment.polarity)  # Result = 1.0
print("Sentiment Subjectivity: ", sentiment.sentiment.subjectivity)  # Result = 1.0
