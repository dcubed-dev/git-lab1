let input = process.argv[2] //must be entered within single quotes (ex: '$9.87')

let cleanInput;

//ensures input is valid
if ((!input)||(input[0] != "$")){console.log("The string must begin with a $")}
else{
    cleanInput = input.replace("$","")

    if (cleanInput[0] == "."){console.log("The string must include a dollar amount")}

    else{
    //split input into dollars and cents
    let dotIndex = cleanInput.indexOf(".")
    if(dotIndex != -1){
        dollars = cleanInput.substring(0,dotIndex)
        cleanInput = cleanInput.substring(dotIndex+1)
    }

    //find values of each denomination
    dollarInt = Number(dollars);
    dollars = [" dollar", " dollars", dollarInt]
    centsInt = Number(cleanInput)

    let quarters = [" quarter", " quarters", Math.floor(centsInt/25)]
    centsInt = centsInt % 25

    let dimes = [" dime"," dimes",Math.floor(centsInt/10)]
    centsInt = centsInt % 10

    let nickels = [" nickel"," nickels",Math.floor(centsInt/5)]
    centsInt = centsInt % 5

    let pennies = [" penny"," pennies",centsInt]

    //for each loop to go thru all denoms and output
    for (x of [dollars,quarters,dimes,nickels,pennies]){
        if(x[2]>0){
            if(x[2]==1){console.log(x[2]+x[0])}
            else{console.log(x[2]+x[1])}
        }
    }

}
}
