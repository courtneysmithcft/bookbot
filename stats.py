#function that accepts the text from the book as a string, and returns the number of words in the string
def count_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    
    return char_count

def sort_on(item):
    return item["num"]


#takes the dictionary of characters and their counts and returns a sorted list of dictionaries
def sort_dictionary(char_count):
    #convert dict to list
    sorted_list = []
    for char,count in char_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    # Sort list of dicts by "num" descending
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
