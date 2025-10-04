from stats import count_words, character_count, sort_dictionary
import sys

#Confirm userpassed the correct arguments to sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


#import file path from user entry
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    



def main():
    filepath = str(sys.argv[1])
    
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