# Assignment Name : Semantic Meaning
# Description : Find 5 word pairs and explain semantic similarity.

import spacy

# Load spaCy medium model (contains 300-dimensional word vectors)
nlp = spacy.load("en_core_web_md")

# 5 word pairs with varying degrees of semantic similarity
word_pairs = [
    ("king", "queen"),
    ("happy", "joyful"),
    ("car", "automobile"),
    ("dog", "computer"),
    ("hot", "cold"),
]

# Explanations for each word pair
explanations = {
    ("king", "queen"):
        "Both are royalty titles sharing the domain of monarchy. They differ in gender "
        "but are used in very similar contexts, so high similarity is expected.",

    ("happy", "joyful"):
        "These are near-synonyms expressing positive emotions. They can be used "
        "interchangeably in most sentences, so very high similarity is expected.",

    ("car", "automobile"):
        "These are exact synonyms — different words with the same meaning. "
        "Their word vectors should be very close, giving high similarity.",

    ("dog", "computer"):
        "These belong to completely different domains (animals vs technology). "
        "They rarely appear in similar contexts, so low similarity is expected.",

    ("hot", "cold"):
        "These are antonyms (opposite meanings) but belong to the same semantic "
        "field (temperature). They often appear in similar contexts, so moderate "
        "similarity is expected — word vectors capture context, not just meaning.",
}

print("=" * 70)
print("           SEMANTIC SIMILARITY EXPLORER")
print("=" * 70)

for word1, word2 in word_pairs:
    # Process each word through spaCy to get its vector
    token1 = nlp(word1)
    token2 = nlp(word2)

    # Compute cosine similarity between the two word vectors
    similarity = token1.similarity(token2)

    # Visual bar
    bar = "█" * int(similarity * 30)

    print(f"\n  Word Pair     : '{word1}' ↔ '{word2}'")
    print(f"  Similarity    : {similarity:.4f}  {bar}")
    print(f"  Explanation   : {explanations[(word1, word2)]}")
    print("-" * 70)

# Overall explanation
print("\n" + "=" * 70)
print("  HOW SEMANTIC SIMILARITY WORKS")
print("=" * 70)
print("""
Semantic similarity measures how close two words are in meaning.
It is computed using Word Vectors (also called Word Embeddings).

1. Word Vectors:
   - Each word is represented as a vector in a high-dimensional space
     (e.g., 300 dimensions in spaCy's 'en_core_web_md' model).
   - These vectors are learned from large text corpora (like Common Crawl).
   - Words that appear in similar contexts get similar vectors.
     e.g., 'king' and 'queen' appear near words like 'throne', 'crown', 'royal'.

2. Cosine Similarity:
   - Measures the angle between two vectors, ignoring magnitude.
   - Formula: cos(θ) = (A · B) / (||A|| × ||B||)
   - Score of 1.0 = identical direction (same meaning)
   - Score of 0.0 = perpendicular (no relation)
   - Score near -1  = opposite direction (rare in practice)

3. Key Observations:
   - Synonyms (happy ↔ joyful)       → HIGH similarity
   - Related words (king ↔ queen)     → HIGH similarity
   - Antonyms (hot ↔ cold)            → MODERATE similarity (shared context)
   - Unrelated words (dog ↔ computer) → LOW similarity

4. Limitation:
   - Word vectors capture co-occurrence, not strict meaning. So antonyms
     like 'hot' and 'cold' still show moderate similarity because they
     appear in similar sentences about temperature.
""")
