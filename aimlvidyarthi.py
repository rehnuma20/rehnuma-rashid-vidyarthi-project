from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.
    
    Polarity is a float value ranging from -1.0 (most negative) to 1.0 (most positive).
    Subjectivity is a float value ranging from 0.0 (very objective) to 1.0 (very subjective).
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity score
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    print(f"\nAnalyzing Text: '{text}'")
    print(f"Polarity Score: {polarity:.2f} (closer to 1.0 is positive, -1.0 is negative)")
    print(f"Subjectivity Score: {subjectivity:.2f} (closer to 1.0 is opinion, 0.0 is fact)")

    # Determine the general sentiment
    if polarity > 0:
        return "Result: Positive Sentiment 😊"
    elif polarity < 0:
        return "Result: Negative Sentiment 😠"
    else:
        return "Result: Neutral Sentiment 😐"

# --- Example Usage ---
statement1 = "he hates her so much that he can kill her."
result1 = analyze_sentiment(statement1)
print(result1)

print("-" * 30)

statement2 = "The previous class was very confusing and  prettydifficult to understand."
result2 = analyze_sentiment(statement2)
print(result2)

print("-" * 30)

statement3 = "The sky is pink and the leaves are brown."
result3 = analyze_sentiment(statement3)
print(result3)

print("-"*30)

statement4 = "I hate Prachi and their friends"
result4 = analyze_sentiment(statement4)
print(result4)

print("-"*30)

statement5 = "when it rains a lot , i feel bad for farmers"
result5 = analyze_sentiment(statement5)
print(result5)

print("-"* 30)

statement6 = "He is a psychopath , i dont know what he even thinks "
result6 = analyze_sentiment(statement6)
print(result6)

print("-"* 30)