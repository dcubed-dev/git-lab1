const userInput = process.argv.slice(2);

// INITIAL INPUT VALIDATION
if (userInput.length === 0) {
  console.log("[ERROR] No input provided.");
  process.exit();
}

// SANITIZE USER INPUT
let userInputSanitized = userInput
  .join(" ")
  .trim()
  .replace(/\"/g, "")
  .split(" ");

let userInputLower = userInputSanitized.map((word) => word.toLowerCase());

// FIND DUPLICATE WORDS
let words = new Map();

for (let word of userInputSanitized) {
  if (
    userInputLower.filter((w) => w === word.toLowerCase()).length > 1 &&
    !words.has(word.toLowerCase())
  ) {
    words.set(word.toLowerCase(), word);
  }
}

// PRINT THE RESULT
words.forEach((word) => console.log(word));
