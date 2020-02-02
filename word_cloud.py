from wordcloud import WordCloud
import matplotlib.pyplot as plt
def generate_wordcloud(text_phrase, title):
    wordcloud = WordCloud(width=800, height=500, max_font_size=110).generate(text_phrase)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title(f'WORDCLOUD FOR {title}')
    plt.show()


generate_wordcloud("oday was a good day. Started off with a good morning run, went out for a jog and later, when i came back,' \
       'I went to work feeling fresh", "Good day")