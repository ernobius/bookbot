from stats import *
import sys

if len(sys.argv) == 2:

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")


    for l in letter_count():
        char = l["char"]
        n = l["num"]
        print(f"{char}: {n} \n")


    print("============= END ===============")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)