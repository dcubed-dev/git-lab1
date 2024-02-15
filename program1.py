import sys
import decimal

#Reads string off command line
DollarAmount = sys.argv[1]


#Error Check
if len(sys.argv) > 2:
    print("Only one argument (money) should be allowed")
    sys.exit(-1)

#Checks if the argument is a valid string
if DollarAmount[0] != '$':
    print('The string must being with a $')
    sys.exit(-1)
elif DollarAmount[1] == '.':
    print('The string must include a dollar amount')
    sys.exit(-1)

#Converts string into money in terms of cents and creates dictionary of coins/dollar
#Also checks to see if string can be convrted
try:
    float(DollarAmount[1:])
except:
    print('Only input numbers after the dollar symbol')
    sys.exit(-1)
DollarAmount = float(DollarAmount[1:]) * 100
Coins = {}

#Error check to see if number is valid
if (DollarAmount < 0 or DollarAmount > 100 * 100):
    print('The dollar amount must be a number 0 - 100')
    sys.exit(-1)
if (DollarAmount % 1 != 0):
    print('Only valid dollar amounts')
    sys.exit(-1)



#Sorts through all the money values and sees how many are inside
if DollarAmount // 100 == 1:
    Coins['Dollar'] = 1
    DollarAmount -= DollarAmount // 100 * 100
elif DollarAmount // 100 > 1:
    Coins['Dollars'] = DollarAmount // 100 
    DollarAmount -= DollarAmount // 100 * 100
DollarAmount = round(DollarAmount)

if DollarAmount // 25 == 1:
    Coins['Quarter'] = 1
    DollarAmount -= DollarAmount // 25 * 25
elif DollarAmount // 25 > 1:
    Coins['Quarters'] = DollarAmount // 25
    DollarAmount -= DollarAmount // 25 * 25
DollarAmount = round(DollarAmount)

if DollarAmount // 10 == 1:
    Coins['Dime'] = 1
    DollarAmount -= DollarAmount // 10 * 10
elif DollarAmount // 10 > 1:
    Coins['Dimes'] = DollarAmount // 10
    DollarAmount -= DollarAmount // 10 * 10
DollarAmount = round(DollarAmount)

if DollarAmount // 5 == 1:
    Coins['Nickel'] = 1
    DollarAmount -= DollarAmount // 5 * 5
elif DollarAmount // 5 > 1:
    Coins['Nickels'] = DollarAmount // 5
    DollarAmount -= DollarAmount // 5 * 5
DollarAmount = round(DollarAmount)

if DollarAmount // 1 == 1:
    Coins['Penny'] = 1
    DollarAmount -= DollarAmount // 1
elif DollarAmount // 1 > 1:
    Coins['Pennies'] = DollarAmount // 1
    DollarAmount -= DollarAmount // 1

for key in Coins:
    print(int(Coins[key]), key)