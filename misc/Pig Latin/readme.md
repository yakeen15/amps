# Translate an English word into Pig Latin
Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix
### Rules
1. For words that start with a **constant** all letters before the initial vowel are placed at the end of the word sequence. Then, an "ay" is added. e.g. "pig" = "igpay"
2. For words that start with a **vowel** an "-way" is added at the end of the word. e.g. "egg" = "eggway"

### Algorithm
- **Input -** a word in english
- **Output -** a word in Pig Latin
- **Steps:** 
1. Ask user for a word
2. Count word length
3. If the first letter of word is a vowel, go to 4. else go to 5
4. Add "-way" to word
5. Add a "-" to word
6. Shift the word to the left by a single letter
7. If the first word of the transformed word is a vowel, go to 8. else go to 6
8. Add "ay" to word
9. If word has no vowel, add "way" to word
10. Print the transformed word
