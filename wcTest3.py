import matplotlib.pyplot as plt

from wordcloud import WordCloud


text = open("wctest.txt",encoding="utf-8").read()

wordcloud = WordCloud(font_path="HMFMPYUN.TTF").generate(text)

# print(wordcloud.words_)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
# plt.show()

import numpy as np
from PIL import Image
from wordcloud import STOPWORDS


alice = np.array(Image.open("alice.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

plt.figure(figsize=(8,8))
plt.imshow(alice,cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
# plt.show()

wc = WordCloud(background_color="white",mask=alice,stopwords=stopwords,font_path="HMFMPYUN.TTF").generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
# plt.show()

import random



def grey_color_func(word, font_size, position, orientation, random_state=int , **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

plt.figure(figsize=(12,12))
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
plt.axis("off")
# plt.show()


from wordcloud import ImageColorGenerator

alice_color = np.array(Image.open("alice_color.png"))


wc = WordCloud(background_color="white",mask=alice_color,stopwords=stopwords,font_path="HMFMPYUN.TTF").generate(text)

img_color = ImageColorGenerator(alice_color)


plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
# plt.show()


plt.figure(figsize=(12,12))
plt.imshow(alice_color, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
#plt.show()

plt.figure(figsize=(12,12))
plt.imshow(wc.recolor(color_func=img_color), interpolation="bilinear")
plt.axis("off")
plt.show()


# https://pinkwink.kr/1029
