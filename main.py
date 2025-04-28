from stats import get_num_words, count_chars, char_sort

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

frank = "books/frankenstein.txt"

frank_results = get_book_text(frank)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {frank}...")
print("----------- Word Count ----------") 

word_count = get_num_words(frank_results)
print(f"Found {word_count} total words")

print("--------- Character Count -------") 
char_count = count_chars(frank_results)

sorted_char = char_sort(char_count)

for item in sorted_char:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")

print("============= END ==============")