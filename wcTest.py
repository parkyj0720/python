from PIL import Image
from wordcloud import WordCloud

import numpy as np

mask = np.array(Image.open("alice.png"))

text = open("wctest.txt",encoding="utf-8").read()

wc = WordCloud(font_path="HMFMPYUN.TTF",background_color="black",max_words=20000,max_font_size=300,mask=mask,colormap="nipy_spectral",).generate(text)

wc.to_file("test2.png")