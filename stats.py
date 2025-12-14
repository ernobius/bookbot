#from main import get_book_text
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    words = get_book_text().split()
    num_words = len(words)
    return num_words

def letter_count():
    char_count = {}
    letters = get_book_text().lower()

    for ch in letters:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    sorted_list = []
    for ch, count in char_count.items():
        if ch.isalpha():
             sorted_list.append({"char": ch, "num": count})

    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    



