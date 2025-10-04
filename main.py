def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    

#function that accepts the text from the book as a string, and returns the number of words in the string
def count_words(text):
    words = text.split()
    count = len(words)

    return print(f"Found {count} total words")


def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    #print(book_text)  # Print the entire contents of the book
    count_words(book_text)




main()