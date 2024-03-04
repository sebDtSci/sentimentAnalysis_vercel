from flask import Flask, request, jsonify,render_template
from model.main import analyse_sentiment, __version__

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['Text']
        product = analyse(text)  # Supposons que cette fonction retourne un prix pour simplifier
        return render_template('index.html', product=product)
    else:
        return render_template('index.html',products="products")

def analyse(text:str)-> dict:
    polarity, subjectivity = analyse_sentiment(text)

    return {'text': text, 'polarity': polarity, 'subjectivity': subjectivity, "model_version" : __version__}

if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.1', port=5001)
    app.run(host='127.0.0.1', port=5001)