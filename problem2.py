import sys

input = ' '.join(sys.argv[1:])
if not input:
    print("You must provide at least one string")
else:
    inputList = input.split()

    lowercaseList = inputList.copy()
    for x in range(len(lowercaseList)):
        lowercaseList[x] = lowercaseList[x].lower()

    output = []
    for x in range(len(lowercaseList)):
        for i in range(len(lowercaseList)):
            if(x!=i):
                if lowercaseList[x] == lowercaseList[i]:
                    found = False
                    for z in range(len(output)):
                        if inputList[x].lower() == output[z].lower():
                            found = True
                    if not found:
                        output.append(inputList[x])


    for x in output:
        print(x)
