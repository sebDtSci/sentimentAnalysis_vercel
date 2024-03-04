from model.main import analyse, analyse_sentiment, __version__
from src.app import analyse as an

def test_analyse():
    assert analyse(0) == 'Neutre'
    assert analyse(-0.9) == 'Negatif'
    assert analyse(0.9) == 'Positif'

def test_analyse_sentiment():
    assert analyse_sentiment('mot') == ('Neutre',0.0)

def test_an():
    assert an('mot') == {'text': 'mot', 'polarity': 'Neutre', 'subjectivity': 0.0, "model_version" : __version__}