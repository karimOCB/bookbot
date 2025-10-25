def get_words_text(content):
    words = content.split()
    return len(words)

def get_characters_text(content):
    characters_num = {}
    for c in content:
        low_c = c.lower()
        if low_c not in characters_num:
            characters_num[low_c] = 0
        characters_num[low_c] += 1
    return characters_num

def get_sorted_chars(characters):
    chars_dicts = []
    for c in characters:
        chars_dicts.append({"char": c, "num": characters[c]})    
    chars_dicts.sort(key=get_num_key, reverse=True)
    return chars_dicts
    
def get_num_key(item):
        return item["num"]