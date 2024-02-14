//Check if there is at least one string
if (process.argv.length === 2) {
    console.error("ERROR: You must provide at least one string")
    process.exit(1)
}

//Split, lowercase, and remove punctuation in string
let originalText = process.argv.slice(2)
originalText = originalText.join(' ')
lowerText = originalText.toLowerCase()

const punctuation = ['.', ',', ';', ':', '!', '?', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '“', '”'];
let text = '';
for (let i = 0; i < lowerText.length; i++) {
    if (!punctuation.includes(lowerText[i])) {
        text += lowerText[i];
    }
}
text = text.split(' ')

wordCount = {}

//Track frequency of each word
for (let i = 0; i < text.length; i++) {
    let word = text[i]
    if (word in wordCount){
        wordCount[word] ++
    }
    else {
        wordCount[word] = 1
    }
}

//Print out words with duplicates
for (let word in wordCount) {
    if (wordCount[word] > 1){
        let index = lowerText.indexOf(word)
        console.log(originalText.slice(index,index+word.length))
    }
}

