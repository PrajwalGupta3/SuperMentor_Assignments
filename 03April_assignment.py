# Assignment Name : NLP Mini App
# Description : Build a chatbot, fake news detector, or keyword extractor.

"""
This script implements a dual-purpose NLP Mini App:
1. Keyword Extractor: Analyzes text to find the most meaningful words by 
   removing 'stop words' and counting frequencies.
2. Smart Chatbot: A simple rule-based bot that uses keyword matching to 
   provide relevant answers to user queries.
"""

import re
from collections import Counter

# Custom list of common English stop words to avoid external dependencies
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "any", "both", "each", "few",
    "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
    "should", "now", "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
    "had", "having", "do", "does", "did", "doing"
}

def clean_text(text):
    """Removes special characters and converts to lowercase."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def extract_keywords(text, top_n=5):
    """Extracts top_n keywords from text."""
    cleaned = clean_text(text)
    words = cleaned.split()
    # Filter out stop words and short words
    filtered_words = [w for w in words if w not in STOP_WORDS and len(w) > 2]
    
    counts = Counter(filtered_words)
    return counts.most_common(top_n)

def chatbot_response(user_input):
    """Simple keyword-based chatbot logic."""
    user_input = clean_text(user_input)
    
    responses = {
        "hello": "Hello! I am your NLP-powered assistant. How can I help you today?",
        "hi": "Hi there! Ready to explore some NLP?",
        "nlp": "NLP stands for Natural Language Processing. It's how computers understand human language!",
        "python": "Python is the best language for NLP and AI development.",
        "assignment": "This is the NLP Mini App assignment for April 3rd.",
        "bye": "Goodbye! Have a great day coding!",
        "thank": "You're welcome!",
        "help": "I can help you extract keywords or answer basic questions about AI/NLP."
    }
    
    # Check if any keyword in responses is in user_input
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
            
    return "That sounds interesting! Could you tell me more about that?"

# --- Main Execution ---

def main():
    print("="*60)
    print("           NLP MINI APP : KEYWORD EXTRACTOR & CHATBOT")
    print("="*60)

    # Part 1: Keyword Extraction Demo
    sample_text = """
    Artificial Intelligence and Machine Learning are transforming the world. 
    NLP, or Natural Language Processing, allows computers to understand, 
    interpret, and generate human language. Python is a popular choice for 
    building these AI models because of its simplicity and powerful libraries.
    """
    
    print("\n[STEP 1] Analyzing Sample Text:")
    print("-" * 30)
    print(f"Text: {sample_text.strip()}")
    
    keywords = extract_keywords(sample_text)
    print("\nTop Keywords Found:")
    for word, freq in keywords:
        print(f" - {word.capitalize()}: {freq} times")

    # Part 2: Chatbot Interaction
    print("\n" + "="*60)
    print("           NLP MINI APP : INTERACTIVE CHATBOT")
    print("="*60)
    print("(Type 'bye' to exit)")
    
    # Pre-defined interaction for demonstration if input() is not feasible
    demo_queries = ["Hello", "What is NLP?", "Is Python good for AI?", "bye"]
    
    for query in demo_queries:
        print(f"\nUser: {query}")
        response = chatbot_response(query)
        print(f"Bot : {response}")
        if query.lower() == "bye":
            break

if __name__ == "__main__":
    main()
