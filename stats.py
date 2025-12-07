def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    text = text.lower()

    chars = {}

    for char in text:
        if not char in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    
    return chars

def sort_on(items):
    return items['num']

def dict_sort(dictionary):
    dictionary.sort(reverse=True, key=sort_on)
    # print(dictionary)