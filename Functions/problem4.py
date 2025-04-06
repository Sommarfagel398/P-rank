def palindrome_checker(sentence):

    char_sentence = ' '.join(char.lower() for char in sentence if char.isalnum())

    if char_sentence == char_sentence[::-1]:
        return "is a palindrome"
    else:
         return "its not"

input_sentence = input("Enter a sentence: ")
result = palindrome_checker(input_sentence)
print(result)
