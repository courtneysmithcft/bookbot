from stats import count_words, character_count, sort_dictionary


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    



def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Word count
    total_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    # Character count
    print("--------- Character Count -------")
    sorted_characters = sort_dictionary(character_count(book_text))
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()