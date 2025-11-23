
Statement Analyzer  A versatile Python program designed to analyze text, categorize statements, and extract key insights. Project Description The Statement Analyzer is a robust text processing tool developed in Python. 
Sentiment Analysis Using TextBlob -
 Overview of the Project
This project analyses the sentiment of a given text input using TextBlob, a simple NLP library in Python.
The program calculates:
Polarity (how positive/negative the sentence is)
Subjectivity (whether the sentence is emotional or factual)
Based on the polarity score, the program outputs whether the sentiment is Positive, Negative, or Neutral.
 Features -
Accepts any text input for sentiment analysis
Computes polarity score (range: –1 to +1)
Computes subjectivity score (range: 0 to 1)
Prints detailed analysis for each sentence
Provides emoji-based sentiment classification
Demonstrates sentiment analysis with multiple test statements
 Technologies / Tools Used -
Python 3
TextBlob (NLP library)
pip (for installing dependencies)
 Steps to Install & Run the Project -
Step 1: Install TextBlob
pip install textblob
Step 2: Install TextBlob corpora
python -m textblob.download_corpora
Step 3: Save your Python file
Example filename: sentiment_analysis.py
Step 4: Run the program
python sentiment_analysis.py
The script will print polarity, subjectivity, and the final sentiment result.
 Instructions for Testing -
You can test the program by:
Editing the sample statements already included in the code
Adding your own custom sentences like:
analyze_sentiment("I love this product!")
analyze_sentiment("This is terrible and disappointing.")
Each test will output:
Polarity
Subjectivity
Sentiment category
 


