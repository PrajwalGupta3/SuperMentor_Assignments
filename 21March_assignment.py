#Assignment Name : Build a Text Cleaner
#Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.

import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Sample text
text = "OMG!!! This movie is sooo goooood 😍🔥. I can't believe this happened!!!"
# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove emojis and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize text
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)
# Clean the sample text
cleaned_text = clean_text(text)
print("Original Text:")
print(text)
print("\nCleaned Text:")
print(cleaned_text)
# The code defines a function `clean_text` that takes a string input and performs several preprocessing steps:
# 1. Converts the text to lowercase.
# 2. Removes punctuation using `str.translate`.
# 3. Removes emojis and special characters using a regular expression.
# 4. Tokenizes the text into words.
# 5. Removes stopwords using NLTK's list of English stopwords.
# Finally, it joins the cleaned words back into a single string and returns it. The sample text is cleaned and printed before and after processing.
