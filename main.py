from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    wordcount = word_count(get_book_text(("./books/frankenstein.txt")))
    print(f"Found {wordcount} total words")
          
main()