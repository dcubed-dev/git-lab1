import sys

if len(sys.argv) < 2: # Check if the user did not provide any words as command line arguments and print an error message if so.
    print("ERROR: You must provide at least one string")
    exit()

# Turn all of the command line arguments into two list of words, one in original
# case and one in all lowercase.
big_string = ' '.join(sys.argv[1:])
words = big_string.split()
lowercase_words = big_string.lower().split()

for word in words:
# Print a word and remove all duplicates of it from the lowercase_words list if
# it appears more than once in lowercase_words.
    if lowercase_words.count(word.lower()) > 1:
        print(word)
        for lowercase_word in lowercase_words:
            if word.lower() == lowercase_word:
                lowercase_words.remove(lowercase_word)