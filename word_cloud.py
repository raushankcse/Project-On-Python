import sys 
import numpy as np
from PIL import Image
import wikipedia  # to extract information
from wordcloud import WordCloud, STOPWORDS

# We wil import stopwords because to remove common words like the a and than here after

a = str(input("Enter the name of which you want to make word cloud: "))
title = wikipedia.search(a)[0]

page = wikipedia.page(title)

text = page.content

print(text)

bg = np.array(Image.open("abcd.jpg"))   # download the backgroun image because we need base on which our words will
unwated_words = set(STOPWORDS)
wordclo = WordCloud(background_color="black",max_words=400, mask=bg, stopwords=unwated_words)
wordclo.generate(text)
wordclo.to_file("imag.png")



