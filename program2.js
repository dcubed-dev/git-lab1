strings = process.argv.slice(2);

if (!strings || !strings.length) {
  console.log("ERROR: You must provide at least one string");
}

let wordCounts = {}; // in format (word in string) : (occurrences of word)

for (let string of strings) {
    let words = string.toLowerCase().split(/\s+/); // /\s+/ detects any white space character, so multiple " " or tabs.
    for (let word of words) {
      if (wordCounts[word] > 0) {
        console.log(word);
      }
      // This line checks if word is already in wordCounts, if it is then +1 to the value. If not, then value stays at 0. 
      wordCounts[word] = (wordCounts[word] || 0) + 1; 
    }
  }