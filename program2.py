import sys

def duplicates(strings):

    """
    finds and prints duplicate words in a list of strings.

    Arguments:
        strings (list): a list of strings provided by the user to check for duplicates

    Returns:
        none
    """

    #check if strings is empty 
    if not strings:
        print("ERROR: You must provide at least one string")
        return

    #word counts is where the program stores the count of words 
    word_counts = {}
    for string in strings:
        #split into substrings
        words = string.split()

        for word in words:
            #convert word to lowercase
            word_lower = word.lower()
            if word_lower not in word_counts:
                #if word is not yet in word count, it will add it 
                word_counts[word_lower] = []
            #if word is already found, the program appends the extra word to that list 
            word_counts[word_lower].append(word)


    #set makes sure that we dont accidentally add duplicates twice to the list 
    duplicates = set()

    #if the length of a world list is more than 1 that means there was a duplicate word, so when it is greater than 1, it is added to the duplicates set
    for word_list in word_counts.values():
        if len(word_list) > 1:
            duplicates.update(word_list)


    for word in duplicates:
        print(word)


#get input from terminal 
args = sys.argv[1:]
duplicates(args)
