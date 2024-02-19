function processInput(input) {
    // make sure the input is in the right format
    let regex = /^\$([1-9]\d*|0)(\.\d{2})?$/;
    if (!regex.test(input)) {
        console.log("Eror: The string must be in the format $X.YZ");
        return;
    }

    //seperate the dollars and cents from the input 
    let splitinput = input.slice(1).split('.');
    let amtdollars = splitinput[0];
    let cents;
    if (splitinput.length > 1) {
        cents = splitinput[1];
    } else {
        cents = '00';
    }
    
    //cast both amounts to int and get the total amount of cents
    let total = parseInt(amtdollars) * 100 + parseInt(cents);

    function sort(totalcents) {
        let dollars = Math.floor(totalcents / 100);
        totalcents = totalcents % 100;
        let quarters = Math.floor(totalcents / 25);
        totalcents = totalcents % 25;
        let dimes = Math.floor(totalcents / 10);
        totalcents = totalcents % 10;
        let nickels = Math.floor(totalcents / 5);
        let pennies = totalcents % 5;
    
        return {
            dollars: dollars,
            quarters: quarters,
            dimes: dimes,
            nickels: nickels,
            pennies: pennies
        };
    }
    
    //log all the denominations
    let denominations = sort(total);
    if (denominations.dollars > 0) console.log(`${denominations.dollars} dollars`);
    if (denominations.quarters > 0) console.log(`${denominations.quarters} quarters`);
    if (denominations.dimes > 0) console.log(`${denominations.dimes} dimes`);
    if (denominations.nickels > 0) console.log(`${denominations.nickels} nickels`);
    if (denominations.pennies > 0) console.log(`${denominations.pennies} pennies`);

}

// Main
if (process.argv.length !== 3) {
    console.log("ERROR: Incorrect number of arguments. Usage: node program.js \"$X.YZ\"");
} else {
    var input = process.argv[2];
    if (!input.startsWith('$')) {
        console.log("ERROR: The string must begin with a $");
    } else {
        processInput(input);
    }
}
