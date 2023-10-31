import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

#  Read a text file and return its content as a string
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return ""

# Split a string into words, excluding punctuation marks and converting to lowercase
def split_text(text):
    words = text.split()
    words = [word.strip(".,!?\"'()[]") for word in words]
    return [word.lower() for word in words]

# Remove stop words from a list of words
def remove_stop_words(words, stop_words):
    return [word for word in words if word not in stop_words]

# Lemmatize a list of words
def lemmatize_words(words_clean):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words_clean]

# Count the frequency of each lemma and return a dictionary
def compute_frequency_words(words_lemmatized):
    word_count = Counter(words_lemmatized)
    return dict(word_count)

# Save a dictionary to a JSON file
def save_words_frequency(words_frequency, file_path="E:/Codebase/src/assignments/word_counts/word_frequency.json"):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(words_frequency, json_file)
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

def main():
    # Step 1: Convert a text file to a string
    file_path = "E:/Codebase/src/assignments/word_counts/exampletext.txt"
    text = read_text_file(file_path)

    if text:
        # Step 2: Split the string into words
        words = split_text(text)

        # Step 3: Remove stop words
        stop_words = set(stopwords.words('english'))
        words_clean = remove_stop_words(words, stop_words)

        # Step 4: Lemmatize the words
        words_lemmatized = lemmatize_words(words_clean)

        # Step 5: Count the frequency of words
        words_frequency = compute_frequency_words(words_lemmatized)

        # Step 6: Save the results to a JSON file
        save_words_frequency(words_frequency, file_path="E:/Codebase/src/assignments/word_counts/word_frequency.json")

if __name__ == "__main__":
    main()