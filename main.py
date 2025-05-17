import sys
from stats import get_num_words, count_chars, char_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = char_sort(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ==============")

main()