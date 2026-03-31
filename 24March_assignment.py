# Assignment Name : Word Importance Explorer
# Description : Use TF-IDF on 5 documents and identify top keywords with explanation.

from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents on different topics
documents = [
    "Machine learning is a branch of artificial intelligence that enables systems to learn and improve from data without being explicitly programmed.",
    "Natural language processing helps computers understand, interpret and generate human language in a meaningful way.",
    "Deep learning uses artificial neural networks with multiple layers to model complex patterns in large amounts of data.",
    "Computer vision is a field of artificial intelligence that trains computers to interpret and understand the visual world from images and videos.",
    "Reinforcement learning is an area of machine learning where an agent learns to make decisions by taking actions in an environment to maximize a reward."
]

# Create TF-IDF vectorizer (stop_words='english' removes common words like 'the', 'is', 'and')
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Get all feature (word) names
feature_names = vectorizer.get_feature_names_out()

# Display top keywords for each document
print("=" * 65)
print("       WORD IMPORTANCE EXPLORER USING TF-IDF")
print("=" * 65)

for doc_index in range(len(documents)):
    print(f"\nDocument {doc_index + 1}:")
    print(f"  \"{documents[doc_index][:70]}...\"")
    print(f"\n  Top 5 Keywords:")

    # Get TF-IDF scores for this document
    scores = tfidf_matrix[doc_index].toarray().flatten()

    # Pair each word with its score and sort descending
    word_scores = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)

    # Print top 5 keywords
    for rank, (word, score) in enumerate(word_scores[:5], 1):
        bar = "█" * int(score * 30)  # simple visual bar
        print(f"    {rank}. {word:20s}  TF-IDF: {score:.4f}  {bar}")

    print("-" * 65)

# Explanation
print("\n" + "=" * 65)
print("  WHAT IS TF-IDF?")
print("=" * 65)
print("""
TF-IDF stands for Term Frequency - Inverse Document Frequency.
It measures how important a word is to a specific document in a collection.

  TF  (Term Frequency)
      = How often a word appears in a document.
      = (Occurrences of word in doc) / (Total words in doc)

  IDF (Inverse Document Frequency)
      = How rare/unique a word is across ALL documents.
      = log(Total number of docs / Number of docs containing the word)

  TF-IDF = TF × IDF

Why it works:
  - Common words (like 'the', 'is') appear everywhere → low IDF → low score.
  - Rare, topic-specific words appear in few docs → high IDF → high score.
  - A word that is frequent in ONE doc but rare overall gets the highest score,
    making it a strong keyword for that document.

Example from our results:
  - 'learning' appears in multiple documents, so its IDF is lower.
  - 'vision' appears only in the Computer Vision document, so its TF-IDF
    score is high for that document, correctly identifying it as a keyword.
""")
