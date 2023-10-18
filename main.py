# Encoding dictionary with all letters of the alphabet
encoding_dict = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
    'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
    't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
}

while True:
    # User Input
    user_input = input("Enter a sentence to encode: ")

    # Tokenization
    tokens = user_input.split()

    # Encoding
    encoded_sentence = []

    for word in tokens:
        encoded_word = ""
        for letter in word:
            if letter.isalpha():  # Handle only alphabetic characters
                encoded_word += encoding_dict.get(letter.lower(), letter)
            else:
                encoded_word += letter
        encoded_sentence.append(encoded_word)

    # Joining and Display
    encoded_result = ' '.join(encoded_sentence)
    print("Encoded sentence: ", encoded_result)

    another_sentence = input("Encode another sentence? (yes/no): ")
    if another_sentence.lower() != 'yes':
        print("Goodbye!")
        break
