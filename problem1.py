import sys

userInput = sys.argv[1:][0]

# INITIAL INPUT VALIDATION

if userInput[0] != '$':
    print('[ERROR] Amount should start with dollar sign ($).')
    sys.exit()

# SEPARATE DOLLARS AND CENTS
amount = userInput[1:]
dollars = amount.split('.')[0]
cents = amount.split('.')[1]

if len(dollars) == 0:
    print('[ERROR] Dollars should have at least one digit.')
    sys.exit()

if len(cents) != 2:
    print('[ERROR] Cents should have 2 digits.')
    sys.exit()

# PRINT THE RESULT
print(f'{dollars} dollars')

coins = ['quarter', 'dime', 'nickel', 'penny']
coins_plural = ['quarters', 'dimes', 'nickels', 'pennies']

cents = int(cents)

for i in range(4):
    coinValue = 0
    if i == 0:
        coinValue = 25
    elif i == 1:
        coinValue = 10
    elif i == 2:
        coinValue = 5
    else:
        coinValue = 1

    coinCount = cents // coinValue
    cents = cents % coinValue
    if coinCount > 0:
        print(f'{coinCount} {coins[i] if coinCount == 1 else coins_plural[i]}')
