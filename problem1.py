import sys

def main(args):
    currency = [("dollar", "dollars", 100), ("quarter", "quarters", 25), ("dime", "dimes", 10), ("nickel", "nickels" , 5), ("penny", "pennies", 1)]
    if len(args) != 1:
        print("Exactly one argument is required: usage `python problem1.py \$X.YZ`")
        
        exit(-1)
    money = args[0]
    assert money[0] == '$', "\nThe input should start with a dollar sign. Make sure to escape this if on linux."
    dollars = money[1:] # remove $
    dollars, cents = dollars.split('.')
    assert len(cents) == 2, "\nThe cent amount should be two digits"
    assert dollars.isdigit(), "\nThe dollar amount should be a number"
    assert 0 <= int(dollars) <= 100, "\nThe dollar amount should be between 0 and 100"
    assert 0 <= int(cents) <= 99, "\nThe cent amount should be between 0 and 99" 
    total = int(dollars) * 100 + int(cents)

    current = 0
    for name, plural_name, value in currency:
        if total >= value:
            count = total // value # find most whole number of currency that fits
            total -= count * value # remove the amount of currency from the total
            name = plural_name if count > 1 else name
            print(f"{count} {name}")
            current += count

if __name__ == "__main__":
    main(sys.argv[1:])