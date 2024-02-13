/**
 * Checks if the user's input is written in the form $X.YZ, where X is the
 * dollar amount and YZ is the cents amount. If the user's input is not in the
 * correct format, print a helpful error message.
 * @param {string} input The user's input.
 * @returns {boolean} A boolean that is true if no errors are found. Does not
 *  return if an error is found.
 */
function checkFormat(input) {
    if (/[a-zA-Z]/.test(input)) { // Regular expression checks if thare are any letters in input.
        console.log("ERROR: The string may not contain any letters.")
    }
    else if (/[^0123456789\$.]/.test(input)) { // Regular expression checks if thare are any unusuable characters in input.
        console.log("ERROR: The string may not contain characters other than numbers, '.', or '$'.")
    }
    else if (input.slice(0, 1) != "$") {
        console.log("ERROR: The string must being with a '$'.")
    }
    else if (/^\$\.\d{2}$/.test(input)) { // Regular expression checks if input begins with "$."
        console.log("ERROR: The string must include a dollar amount.")
    }
    else if (/^\$\d+\.?$/.test(input)) { // Regular expression checks if input ends in "." or a number.
        console.log("ERROR: The string must include a cent amount.")
    }
    else if (!/^\$\d+\.\d{2}$/.test(input)) { // Regular expression checks if input does not follow $X.YZ format.
        console.log("ERROR: The string must be in the format $X.YZ.")
    }
    else {
        return true
    }
}

/**
 * Converts a string representing a money amount in the form $X.YZ to cents.
 * @param {string} dollarsCents The money amount in the form $X.YZ.
 * @returns {number} The money amount as number of cents.
 */
function convertToCents(dollarsCents) {
    let numbers = dollarsCents.slice(1)
    let cents = Math.round(parseFloat(numbers) * 100)
    return cents
}

/**
 * Finds the least amount of dollars, quarters, nickels, dimes, and pennies
 * needed to make up some number of cents.
 * @param {number} cents The number of cents needed to be converted into coins
 * @returns {object} An array that contains the number of dollars, quarters,
 *  nickels, dimes, and pennies needed to make up some amount of cents, in that
 *  order.
 */
function findCoinCounts(cents) {
    let remainingCents = cents
    let coinValues = [100, 25, 10, 5, 1]
    let coinCounts = []
    for (let i = 0; i < 5; i++) {
        /*
        For every type of coin, count the maximum number of coins that can
        fit in the cents value, and record that number in the coinCounts array.
        */
        let coinValue = coinValues[i]
        coinCount = Math.floor(remainingCents / coinValue)
        coinCounts.push(coinCount)
        remainingCents -= (coinCount * coinValue)
    }
    return coinCounts
}

/**
 * Prints the number of dollars, quarters, dimes, nickels, and pennies needed to
 * make up some amount of money. Does not print coins that are not used.
 * @param {object} coinCounts An array that contains the number of dollars,
 *  quarters, nickels, dimes, and pennies needed to make up some amount of cents, in that
 *  order.
 */
function printCoins(coinCounts) {
    coinStrings = [" dollar", " quarter", " dime", " nickel", " penn"]
    for (let i = 0; i < 5; i++) {
        if (i == 4) { // Print singular or plural form of the penny if it appears.
            if (coinCounts[i] == 1) {
                console.log(coinCounts[i] + coinStrings[i] + "y")
            }
            else if (coinCounts[i] > 1) {
                console.log(coinCounts[i] + coinStrings[i] + "ies")
            }
        }
        else { // Print singular or plural forms of all other coins if they appear.
            if (coinCounts[i] == 1) {
                console.log(coinCounts[i] + coinStrings[i])
            }
            else if (coinCounts[i] > 1) {
                console.log(coinCounts[i] + coinStrings[i] + "s")
            }
        }
    }
}


let input = process.argv[2]
if (checkFormat(input)) {
    let cents = convertToCents(input)
    let counts = findCoinCounts(cents)
    printCoins(counts)
}