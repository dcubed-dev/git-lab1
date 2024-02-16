import sys

args = sys.argv[1:]
example = "python3 Program1.py $1.25"

if len(args) > 1:
    print(f"Too many arguments! Ex: `{example}`")
    exit()

if len(args) == 0:
    print(f"Please use one argument! Ex: `{example}`")
    exit()

dollar_amount = args[0]

if (dollar_amount[0] != "$"):
    print(f"ERROR: The string must begin with a \"$\"! Ex: `{example}`")
    exit()

if (dollar_amount[1].isdigit() == False):
    print(f"ERROR: The string must include a dollar amount! Ex: `{example}`")
    exit()

parsed = dollar_amount[1:].split(".")
dollars = parsed[0]
cents = parsed[1]

if (int(dollars) < 0):
    print(f"ERROR: The dollar amount must be at least 0! Ex: `{example}`")
    exit()

if (int(dollars) > 100):
    print(f"ERROR: The dollar amount must be less than or equal to $100! Ex: `{example}`")
    exit()

# convert cents to coin counts
curr_cents = int(cents)
coin_dict = {"quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}

for coin in coin_dict.keys():
    # floor div so we don't use fractions of a coin
    count = curr_cents // coin_dict[coin]
    # set the new value of curr_cents to the remainder
    curr_cents = curr_cents % coin_dict[coin]
    if (count != 0):
        print(f"{count} {coin}")
    