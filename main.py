import sys 

from stats import num_of_words
from stats import num_of_char
from stats import chars_dict_to_sorted_list

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = num_of_words(book_text)
    char_count = num_of_char(book_text)
    char_list = chars_dict_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in char_list:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()

