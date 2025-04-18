from stats import get_num_words, count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

frank = "books/frankenstein.txt"

frank_results = get_book_text(frank)

word_count = get_num_words(frank_results)
print(f"{word_count} words found in the document")

char_count = count_chars(frank_results)
print(char_count)