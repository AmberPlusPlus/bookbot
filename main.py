from stats import word_count, char_count, dict_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def main():

    bookfile = "books/frankenstein.txt"
    text = get_book_text(bookfile)

    wordcount = word_count(text)
    charcount = char_count(text)
    # print(charcount)

    dict_list = []
    for entry in charcount:
        if not entry[0].isalpha():
            continue
        #print(entry[0])
        dict_list.append({"char": entry[0], "num": charcount[entry[0]]})

    dict_sort(dict_list)

    # print(dict_list)

    # output

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for entry in dict_list:
        #print(entry)
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()