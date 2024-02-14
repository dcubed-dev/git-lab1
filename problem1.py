import sys

def main(money_str):
    """
    Prints out the minimum number of coins to make a dollar amount, i.e $4.42

    Args:
        money_str: A string of the form $X.YZ where X <= 100, and Y and Z are both integers 0 <= x <= 9

    Returns:
        None, has side effect of printing

    Raises:
        AssertationError if input is not valid, may also exit
    """
    currency = [("dollar", "dollars", 100), ("quarter", "quarters", 25), ("dime", "dimes", 10), ("nickel", "nickels" , 5), ("penny", "pennies", 1)]
    if len(money_str) != 1:
        print("Exactly one argument is required: usage `python problem1.py \$X.YZ`")
        exit(-1)
    money = money_str[0]
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
    main(sys.argv[1:][0])