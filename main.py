import sys
from stats import get_words_text, get_characters_text, get_sorted_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_words_text(content)
    num_chars = get_characters_text(content)
    ordered_chars = get_sorted_chars(num_chars)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count ------- """)
    for item in ordered_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()