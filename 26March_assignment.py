# Assignment Name : Movie Review Analyzer
# Description : Build a simple sentiment analyzer and test on 5 reviews.

from textblob import TextBlob

# 5 movie reviews (mix of positive, negative, and neutral)
reviews = [
    "This movie was absolutely fantastic! The acting was superb and the storyline kept me engaged from start to finish.",
    "Terrible waste of time. The plot made no sense and the acting was wooden and unconvincing throughout.",
    "An average film with some decent moments but nothing particularly memorable. It was okay I guess.",
    "I loved every minute of this masterpiece! The cinematography was breathtaking and the soundtrack was beautiful.",
    "The worst movie I have ever seen. Boring, predictable, and the special effects looked cheap and outdated."
]

def analyze_sentiment(text):
    """Analyze the sentiment of a given text using TextBlob."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity         # -1 (negative) to +1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

    if polarity > 0.1:
        label = "Positive ✅"
    elif polarity < -0.1:
        label = "Negative ❌"
    else:
        label = "Neutral  ➖"

    return label, polarity, subjectivity

# Run the analyzer
print("=" * 70)
print("          MOVIE REVIEW SENTIMENT ANALYZER")
print("=" * 70)

for i, review in enumerate(reviews, 1):
    label, polarity, subjectivity = analyze_sentiment(review)

    print(f"\nReview {i}:")
    print(f"  \"{review}\"")
    print(f"  Sentiment    : {label}")
    print(f"  Polarity     : {polarity:+.4f}   (range: -1 negative ... +1 positive)")
    print(f"  Subjectivity : {subjectivity:.4f}    (range: 0 objective ... 1 subjective)")
    print("-" * 70)

# Summary stats
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)
positive = sum(1 for r in reviews if analyze_sentiment(r)[1] > 0.1)
negative = sum(1 for r in reviews if analyze_sentiment(r)[1] < -0.1)
neutral  = len(reviews) - positive - negative
print(f"  Total Reviews : {len(reviews)}")
print(f"  Positive      : {positive}")
print(f"  Negative      : {negative}")
print(f"  Neutral       : {neutral}")

# Explanation
print("\n" + "=" * 70)
print("  HOW IT WORKS")
print("=" * 70)
print("""
This analyzer uses TextBlob, a Python library built on top of NLTK.

1. Polarity Score (-1 to +1):
   - Measures how positive or negative the text is.
   - Words like 'fantastic', 'loved', 'beautiful' push the score positive.
   - Words like 'terrible', 'boring', 'worst' push the score negative.

2. Subjectivity Score (0 to 1):
   - Measures whether the text is factual (objective) or opinion-based (subjective).
   - Movie reviews are typically high in subjectivity since they express opinions.

3. Approach - Lexicon-Based:
   - TextBlob has a built-in dictionary where each word has a pre-assigned
     polarity and subjectivity value.
   - It also handles modifiers: 'not good' flips polarity, 'very good' intensifies it.
   - The final score is an average of all word-level scores in the text.

Limitations:
   - Sarcasm is not detected (e.g., "Oh great, another boring sequel" may score positive).
   - Context-dependent meanings are missed.
   - For production use, ML-based models (BERT, RoBERTa) are more accurate.
""")
