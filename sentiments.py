from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence) # obtain polarity index of given sentence.
    # produces the index of the -ve, +ve, neutral and compound sentiment
    # the compound score is a sum of all lexicon ratings normalized between -1(very negative) to 1 (very positive)
    max_val = max(score["neu"], score["neg"], score["pos"])
    max_sentiment = ''
    full_names = {"neg": "Negative" , "pos":"Positive", "neu":"Neutral"}
    for index, value in score.items():
        if value == max_val:
            max_sentiment = index

    return f'Below are the sentiment scores of the query. \n Neutral score: {score["neu"]}\n ' \
           f'Negative score: {score["neg"]} \n Positive score: {score["pos"]}\n' \
           f'The general sentiment is {full_names[max_sentiment]} - {max_val}'