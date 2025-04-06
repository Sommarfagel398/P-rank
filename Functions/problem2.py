def longest_word(sentence):
    word = sentence.split()
    longest = ''

    for word in word:
        if len(word) > len(longest):
            longest = word
    return longest

input_sentence = input("Enter a sentence")
print("Longest word:",longest_word(input_sentence))

