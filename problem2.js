var arguments = process.argv;
if (arguments.length < 3) {
    console.log('ERROR: You must provide at least one string');
    return;
}
arguments = arguments.slice(2); 
const word_map = new Map();

arguments.forEach((word) => {
    // so I am considering what to do in the case where you have '“' or '”' in the word
    // in your examples, 'Panda”' matched with panda despite the quotes
    // this seems to go against 'A word is indicated by a sequence of characters separated by whitespace.'
    // as ” is a character and not whitespace so it should be part of the word

    // I will follow the test cases and assume that the quotes are not part of the word
    word = word.toLowerCase();
    word = word.replace(/[^a-zA-Z]/g, '');

    if (word_map.has(word)) {
        word_map.set(word, word_map.get(word) + 1);
    } else {
        word_map.set(word, 1);
    }
});

word_map.forEach((value, key) => {
    if (value > 1) {
        console.log(key);
    }
});
//console.log(word_map);