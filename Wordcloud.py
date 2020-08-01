# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:48:32 2020

@author: Himanshu Gupta
"""
#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ("Ayushi Aditi Ayushi Akhsay Alex Ankita Ankita Shweta Shweta")
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
