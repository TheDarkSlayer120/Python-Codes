def analyze_text(text_inputed_by_user):
    number_of_vowels = 0
    number_of_consonants = 0
    number_of_digits = 0
    number_of_punctuation = 0
    number_of_whitespace = 0

    for letter in text_inputed_by_user:
        letter = letter.lower()

        if letter in "aeiou":
            number_of_vowels += 1
            continue
        if letter in "bcdfghjklmnpqrstvwxyz":
            number_of_consonants += 1
            continue
        if letter in "0123456789":
            number_of_digits += 1
            continue
        if letter in " \t":
            number_of_whitespace += 1
            continue
            
        number_of_punctuation += 1

    return number_of_vowels, number_of_consonants, number_of_digits, number_of_punctuation, number_of_whitespace

text_inputed_by_user = input("Enter some text: ")

num_vowels, num_consonants, num_digits, num_punctuation, num_whitespace = analyze_text(text_inputed_by_user)
print(" ")
print("Analysis Results:")
print("-----------------")
print(">The number of vowels: ", (num_vowels))
print(">The number of consonants: ", (num_consonants))
print(">The number of digits: ", (num_digits))
print(">The number of punctuation characters: ", (num_punctuation))
print(">The number of whitespace characters (space and tab): ", (num_whitespace))
