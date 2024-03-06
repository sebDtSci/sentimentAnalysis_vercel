from textblob import TextBlob

__version__ = "0.1.0"

def analyse(score:float)-> str:
    """ This function will return the valence in string based on the score,
    if score < 0 -> Neg, > 0 -> Pos, = 0 -> Neutral

    Args:
        score (float): get the score given by blob.sentiment

    Returns:
        str: return a string in this list (Negatif, Neutre, Positif)
    """
    if score < 0:
        return 'Negatif'
    elif score == 0:
        return 'Neutre'
    else:
        return 'Positif'

def analyse_sentiment(text:str) -> tuple[str,float]:
    """This function return the result of the sentiment analisys

    Args:
        text (str): the sentence

    Returns:
        tuple[str,float]: return sentence and the score
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    sent = analyse(sentiment.polarity)
    return sent, sentiment.subjectivity