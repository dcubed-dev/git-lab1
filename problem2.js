let arguments = process.argv;
if (arguments.length < 3) {
    console.log('ERROR: You must provide at least one string');
    return;
}
arguments = arguments.slice(2); 
split_arguments = []
for (let arg of arguments) {
    // woah the "spead" operator is really neat
    // split returns an array and ... (functionally) appends each element to split_arguments without another for loop 
    // probably equal to concat? this avoids a copy which totally doesn't matter here
    split_arguments.push(...arg.split(" "));
}

// console.log(split_arguments);
// has key of lowercase word, value of [original case, number of occurances]
const word_map = new Map();

for (let word of split_arguments) {
    // console.log(word);
    word_lower = word.toLowerCase();

    // only want to update occurances, not original case of word after we find a new word
    if (!word_map.has(word_lower)) {
        word_map.set(word_lower, [word, 1]);
    } 
    else {
        updated_count = word_map.get(word_lower);
        updated_count[1] += 1
        word_map.set(word_lower, updated_count)
    }
}
//console.log(word_map);

for (let kv of word_map.entries()) {
    occurances = kv[1];
    if (occurances[1] > 1) {
        console.log(occurances[0]);
    }
}