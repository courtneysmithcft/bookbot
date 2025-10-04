#function that accepts the text from the book as a string, and returns the number of words in the string
def count_words(text):
    words = text.split()
    count = len(words)

    return print(f"Found {count} total words")
