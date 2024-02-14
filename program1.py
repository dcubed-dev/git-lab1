import sys

money = sys.argv[1]

# Replaces the first instance only of "$" and ".". Nothing happens if they don't exist.
money1 = (money.replace("$", "", 1).replace(".", "", 1))

if money1.isdigit():
    sum = int(money1) # Makes money1 an integer if money1 is a number. 
    if sum < 0 or sum > 10000:
        print("Error, value must be between 0 and 100 dollars.")
    else:
        # Dictionary to store the value of each currency.
        coins = {
            "Dollar": sum // 100,   
            "Quarter": (sum % 100) // 25,
            "Dime": (sum % 25) // 10,
            "Nickel": (sum % 10) // 5,
            "Penny": (sum % 5)
        }
        # Another format check, but for the initial variable.
        if money[0] != "$" or ("." not in money):
            print("Error please provide in the correct format '$x.yz' for x, y, z in positive integers.")
        else:
            # For key, value in coins
            for i, j in coins.items():
                if j > 0: # Only if the value is greater than 0 it gets printed. E.g. 0 dollars won't get printed.
                    # To correctly grammatically format (dollar vs dollars):
                    if j == 1: 
                        print(f"{j} {i}")
                    else: # j > 1 formatting for duplicate currencies.
                        if i == "Penny":
                            print(f"{j} Pennies") # Need to print j pennies, not j penny if multiple exist.
                        else:
                            print(f"{j} {i}s") # Adding s at the end works for every other currency.

        
else:
    # If amount is not in valid format:
    print("Error please provide in the correct format '$x.yz' for x, y, z in positive integers.")