# -*- coding: utf-8 -*-
"""real-time-sentiment-analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kWUfcGPhmMVbjbm37vLBI98xjzyi77Ii
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

user_input = input("Please Rate our services>>:")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
print(score)

if(score["neg"]!=0):
  print("Negative")
else:
  print("Positive")
