def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    word_list = text.split()
    return len(word_list)

def main():

    wordcount = word_count(get_book_text(("./books/frankenstein.txt")))
    print(f"Found {wordcount} total words")
          
main()