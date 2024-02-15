//Creates json of lower case letters indicating capitalized string, and array of letters that are printed out
let letters = {} 
let rtn = []

//Error case
if (process.argv.length == 2){
    console.log('ERROR: You must provide at least one string')
    return
}

/**
 * @params String with spaces in it
 * 
 * 
 * Sorts duplicates into the array and  words into the json,
 * but accounts for the string being multiple words with spaces inbetween
 * 
 */
function SpacedString(Sentence){
    let input = ''
    for (let i = 0; i < Sentence.length; i++){
        if (Sentence[i] == ' '){
            if (Object.hasOwn(letters, input.toLowerCase())){
                rtn.push(letters[input.toLocaleLowerCase()])
            }else{
                letters[input.toLowerCase()] = input
            }
            input = ''
        }else{
            input += Sentence[i]
        }
    }
    if (Object.hasOwn(letters, input.toLowerCase())){
        rtn.push(letters[input.toLocaleLowerCase()])
    }else{
        letters[input.toLowerCase()] = input
    }
}

//Adds all duplicates to array
for (let i = 2; i < process.argv.length; ++i) {
    LowercaseString = process.argv[i].toLowerCase()
    Word = process.argv[i]
    if (Word.includes(' ')){
        SpacedString(Word)
    }
    else if (Object.hasOwn(letters, LowercaseString)){
        if (rtn.includes(letters[LowercaseString]) == false)
            rtn.push(letters[LowercaseString])
    }
    else{
        letters[LowercaseString] = Word
    }
}

//Prints out all duplicate strings
for (let i = 0; i < rtn.length; i++){
    console.log(rtn[i])
}