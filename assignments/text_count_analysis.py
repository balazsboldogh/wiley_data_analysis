import string

def convert_lowercase(text):
    return text.lower()

def split_words(text):
    words = text.split()
    return words

def count_words(text):
    words =  split_words(text)
    return len(words)

def count_distinct_words(text):
    words = split_words(text)
    distinct_words = set(words)
    return len(distinct_words)

def count_each_word(text):
    words = split_words(text)
    word_count = {}

    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count

def remove_punc(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text

def analyze_text(text):
    lowercase_text = convert_lowercase(text)
    text_without_punctuation = remove_punc(lowercase_text)
    word_count = count_words(text_without_punctuation)
    distinct_word_count = count_distinct_words(text_without_punctuation)
    each_word_count = count_each_word(text_without_punctuation)

    print("Original Text:\n", text)
    print("\nText in Lowercase:\n", lowercase_text)
    print("\nText Without Punctuation:\n", text_without_punctuation)
    print("\nTotal Word Count:", word_count)
    print("Distinct Word Count:", distinct_word_count)
    print("\nWord Frequencies:")
    for word, count in each_word_count.items():
        print(f"{word}: {count}")

    return each_word_count

text = "imagine a vast sheet of paper on which straight lines, triangles, squares, pentagons, hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows — only hard and with luminous edges — and you will then have a pretty correct notion of my country and countrymen. alas, a few years ago, i should have said my universe: but now my mind has been opened to higher views of things."

word_freq = analyze_text(text)
print("\nWord Frequencies as a Dictionary:")
print(word_freq)