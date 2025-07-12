def words_in_document(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_count(text):
    characters = {}
    for char in text:
        character = char.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


