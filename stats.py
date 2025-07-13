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
    
def sort_on(items):
    return items["num"]
    
def sorted_list(characters):
    char_list = []
    for key in characters:
        char_list.append({"char": key, "num": characters[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


