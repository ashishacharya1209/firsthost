# Function to check if a word is in a sentence
def find_word_in_sentence(sentence, word):
    # Split the sentence into words
    words = sentence.split()
    
    # Check if the word is in the list of words
    if word in words:
        return f"The word '{word}' is present in the sentence."
    else:
        return f"The word '{word}' is not present in the sentence."

# Take input from the user
sentence = input("Enter a sentence: ")
word = input("Enter the word to find: ")

# Call the function and print the result
result = find_word_in_sentence(sentence, word)
print(result)
