from flask import Flask, request, render_template
from model.main import analyse_sentiment, __version__

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Processes GET and POST requests on the '/' root route.

    For a GET request, displays an HTML page without preloaded product data.
    For a POST request, extracts the text submitted via the form, performs an analysis (for example, calculates a price based on the text) and returns the same HTML page with the product data (the result of the analysis) included.

    Returns:
        str: The HTML content of the home page, with or without the product data included, depending on whether the request is GET or POST.
    """
    if request.method != 'POST':
        return render_template('index.html',products="products")
    text = request.form['Text']
    product = analyse(text)
    return render_template('index.html', product=product)

def analyse(text:str)-> dict:
    """Returns the sentence analysis

    Args:
        text (str): the sentence
    Returns:
        dict: return sentence, polarity, subjectivity and the model version
    """
    polarity, subjectivity = analyse_sentiment(text)

    return {'text': text, 'polarity': polarity, 'subjectivity': subjectivity, "model_version" : __version__}

if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.1', port=5001)
    app.run(host='127.0.0.1', port=5001)