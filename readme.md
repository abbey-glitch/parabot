This project is a simple Natural Language Processing (NLP)-powered chatbot API built with Flask and NLTK. Here's a breakdown of its components and functionality:

🔧 Tech Stack
Flask – For building RESTful API endpoints.

NLTK (Natural Language Toolkit) – For text processing and basic NLP tasks.

CSV – Stores predefined question patterns and responses.

🧠 What It Does
It performs text analysis and provides responses to questions through two API endpoints:

1. /ask Endpoint
Accepts a question in JSON (e.g., {"ask": "What's your name?"}).

Returns the NLP analysis of the input:

Sentence tokenization

Word tokenization

Stopword removal

Lemmatization

POS tagging

Named Entity Recognition (NER)

✅ Useful for understanding and debugging how text is interpreted.

2. /answer Endpoint
Reads question patterns from a responses.csv file.

Compares the user input with each question pattern.

If it finds a match, it returns the predefined answer.

If no match is found, it returns a fallback message.

✅ Useful for building a basic rule-based chatbot.

🗃️ responses.csv File
A CSV file that contains:

question_pattern,response
what is your name?,My name is ParaBot!
how are you?,I'm doing great, thank you!
The bot checks if the user input contains any of the question_pattern entries and replies accordingly.

📦 Key NLP Features Used
Sentence & Word Tokenization: Splits input into smaller parts.

Stopword Removal: Removes common words (e.g., "is", "and").

Lemmatization: Reduces words to base form (e.g., "running" → "run").

POS Tagging: Assigns parts of speech (noun, verb, etc.).

Named Entity Recognition (NER): Identifies names, locations, etc.

🧪 Example Use Case
User Input:

{"ask": "Where is the capital of France?"}
Output (from /ask):


{
  "sentences": ["Where is the capital of France?"],
  "tokens": ["Where", "is", "the", "capital", "of", "France", "?"],
  "filtered": ["Where", "capital", "France"],
  "lemmatized": ["Where", "capital", "France"],
  "entities": "(S ...)"  // Output of named entity tree as string
}
