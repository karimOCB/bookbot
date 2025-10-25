import os
from stats import get_words_text, get_characters_text, get_sorted_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = os.path.join("books", "frankenstein.txt")
    content = get_book_text(book_path)
    num_words = get_words_text(content)
    num_chars = get_characters_text(content)
    ordered_chars = get_sorted_chars(num_chars)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count ------- """)
    for item in ordered_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()