strings = process.argv.slice(2);

// Check if there are no strings provided or if the array is empty
if (!strings || !strings.length) {
  console.log("ERROR: You must provide at least one string");
}
let wordCounts = new Map();
let sentence = strings.join(" ").split(" ");

for (let word of sentence) {
  // Convert the word to lowercase for case-insensitive comparison
  if (wordCounts.has(word.toLowerCase())) {
    // If the word already exists in the wordCounts object, increment its count by 1
    wordCounts.get(word.toLowerCase())[1] += 1;
  } else {
    // If the word doesn't exist in the wordCounts object, add it with a count of 1
    wordCounts.set(word.toLowerCase(), [word, 1]);
  }
}

for (let word of wordCounts.keys()) {
  // Check if the count of the word is greater than or equal to 2
  if (wordCounts.get(word)[1] >= 2) {
    // If the count is greater than or equal to 2, print the word
    console.log(wordCounts.get(word)[0]);
  }
}
