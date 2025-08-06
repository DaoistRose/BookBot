#! /usr/bin/env python3

from stats import get_num_words, get_num_chars, sorted_dict
import sys

# function to return the contents of a file as a string
# with block used to open a file and automatically close it once exited
# .read() method reads the contents of the file into a string
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


# main function to execute the script
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_string = (get_book_text(filepath))
    word_count = get_num_words(book_string)
    char_count = get_num_chars(book_string)
    sorted_char_count = sorted_dict(char_count)
    print('============ BOOKBOT ============\n')
    print(f'Analyzing book found at {filepath}\n')
    print('------------ Word Count ------------\n')
    print(f'Found {word_count} total words\n')
    print('------------ Character Count ------------\n')
    for item in sorted_char_count:
        print(f'{item["char"]}: {item["num"]}')
    print('\n============ END ============')

if __name__ == '__main__':
    main()
