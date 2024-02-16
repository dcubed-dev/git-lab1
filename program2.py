import sys

words = " ".join(sys.argv[1:]).split(" ")
words_lower = [word.lower() for word in words]

if (len(words) == 0):
    print("ERROR: Provide at least one string.")
    exit()

duplicated = []
for word in words:
    if words_lower.count(word.lower()) > 1:
        # I don't wanna talk about it...
        if (not (word in duplicated)) and not ((word.lower() in [word.lower() for word in duplicated])):
            duplicated.append(word)

print("\n".join(duplicated))