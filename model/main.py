from textblob import TextBlob

__version__ = "0.1.0"

def analyse(score:float)-> str:
    if score < 0:
        return 'Negatif'
    elif score == 0:
        return 'Neutre'
    else:
        return 'Positif'

def analyse_sentiment(text:str) -> tuple[str,float]:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    sent = analyse(sentiment.polarity)
    return sent, sentiment.subjectivity