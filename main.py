def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = words_in_document(text)
    print(f"{word_count} words found in the document")
    character_dictionary = character_count(text)
    print(character_dictionary)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import words_in_document, character_count

main()
