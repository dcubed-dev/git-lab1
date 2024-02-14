import sys

#Checks to see if there is one string
if (len(sys.argv) != 2):
    print("ERROR: Provide only one string")
    exit(1)

#Checks to see if there is a dot
money = sys.argv[1]
if not ("." in money):
    print("ERROR: The string must be in '$X.YZ' format")
    exit(1)

split = money.split(".")

#Checks to see if there is a dollar sign
if not ("$" in split[0]):
    print("ERROR: The string must start with a $")
    exit(1)

#Checks to see if there is a dollar amount
if (len(split[0]) == 1):
    print("ERROR: The string must include a dollar amount")
    exit(1)

#Checks to see if there is two digits for cents
if (len(split[1]) != 2):
    print("ERROR: The string must be in '$X.YZ' format")
    exit(1)

dollarString = split[0]
centString = split[1]

#Checks to see if dollar amount is an integer
try:
    dollars = int(dollarString[1:])
except:
    print("ERROR: Dollars must be an integer")
    exit(1)

#Checks to see if cents amount is an integer
try:
    cents = int(centString)
except:
    print("ERROR: Cents must be an integer")
    exit(1)

#Checks if dollar amount is between 0 and 100 inclusive
if (dollars > 100 or dollars < 0):
    print("ERROR: Dollars must be between 0 and 100 inclusive")
    exit(1)

#Print amount of dollars
if dollars > 1:
    print(dollars, "dollars")
if dollars ==  1:
    print(dollars, "dollar")

#Print amount of quarters
if cents >= 25:
    quarters = int(cents/25)
    if quarters > 1:
        print(quarters, "quarters")
    else:
        print(quarters, "quarter")
    cents %= 25

#Print amount of dimes
if cents >= 10:
    dimes = int(cents/10)
    if dimes > 1:
        print(dimes, "dimes")
    else:
        print(dimes, "dime")
    cents %= 10

#Print amount of nickels
if cents >= 5:
    nickels = int(cents/5)
    if nickels > 1:
        print(nickels, "nickels")
    else:
        print(nickels, "nickel")
    cents %= 5

#Print amount of pennies
if cents > 1:
    print(cents, "pennies")
if cents == 1:
    print(cents, "penny")
