word_given = input("Please input a word: ").lower()
word_reversed = word_given[::-1]
if word_given == word_reversed:
    print(f"The word {word_given} is a palindrome.")
else:
    print(f"The word {word_given} is not a palindrome.")
