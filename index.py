from flask import Flask, jsonify, request

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk

import nltk
import csv
import numpy as np

# download nltk resources
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
# nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

app = Flask(__name__)


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def process_text(text):
    # Sentence tokenization
    sentences = sent_tokenize(text)

    # Word tokenization
    words = word_tokenize(text)

    # Stopword removal
    filtered_words = [w for w in words if w.lower() not in stop_words and w.isalpha()]

    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]

    # POS tagging
    pos_tags = pos_tag(lemmatized)

    # Named Entity Recognition
    entities = ne_chunk(pos_tags)

    return {
        "sentences": sentences,
        "tokens": words,
        "filtered": filtered_words,
        "lemmatized": lemmatized,
        "entities": str(entities)
    }


# Load responses from CSV
def load_responses():
    responses = []
    with open("responses.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            responses.append((row['question_pattern'].lower(), row['response']))
    return responses

# answers endpoint
@app.route("/ask", methods=["GET", "POST"])
def bot():
    question = request.json["ask"]
    feed = process_text(question)
    return jsonify(feed)


# Use CSV to get appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    for pattern, reply in load_responses():
        if pattern in user_input:
            return reply
    return "I'm not sure how to answer that yet, but I analyzed your input!"

@app.route("/answer", methods=["GET", "POST"])
def answer():
    data = request.get_json()
    user_input = data.get("user_input", "")
    response = get_response(user_input)
    return jsonify({"reply": response})

# run app
if __name__ == "__main__":
	app.secret_key = '528491@JOKER'
	app.debug = True
	# manager = Manager(app)
	#manager.secret_key = '528491@siva'
	# manager.run()
	app.run()