from stats import *
import sys

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents


def main():
    # print(get_book_text("books/frankenstein.txt"))
    # print(get_word_count("books/frankenstein.txt"))
    # print()
    # print(char_count)
    # print()
    # print()
    # display_book_stats(char_count)

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_word_count(sys.argv[1]))
    print("--------- Character Count -------")
    char_count = get_char_count(sys.argv[1])
    char_count_formatted(char_count)
    print("============= END ===============")
main()