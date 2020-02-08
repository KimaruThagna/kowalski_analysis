from wordcloud import WordCloud
import os
import matplotlib.pyplot as plt
def generate_wordcloud(text_phrase, title, fname):
    wordcloud = WordCloud(width=800, height=500, max_font_size=110, background_color='white').generate(text_phrase)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title(title)
    wordcloud.to_file(fname)

