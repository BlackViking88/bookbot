def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = words_in_document(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_dictionary = character_count(text)
    sort_list = sorted_list(character_dictionary)
    for entry in sort_list:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============") 

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import words_in_document, character_count, sort_on, sorted_list

main()

