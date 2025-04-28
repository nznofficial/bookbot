def get_num_words (text):
    num_words = text.split()
    count_words = len(num_words)
    return count_words

def count_chars(text):
    result_dic = {}
    for char in text:
        if char.lower() in result_dic:
            result_dic[char.lower()] += 1
        else:
            result_dic[char.lower()] = 1

    return result_dic

def sort_on(dict):
    return dict["num"]

def char_sort(char_counts):
    char_list = []
    for character, count in char_counts.items():
        char_list.append({"char":character, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
