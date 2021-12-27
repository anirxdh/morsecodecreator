morse_code = {"a": ". _", "b": "_ . . .", "c":"_ . _ .", "d":"_ . .", "e":".", "f": ". . _ .", "g": "_ _ .", "h":". . . .", "i":". .", "j":". _ . .", "k":"_ . _", "l":". _ _ _", "m":"_ _", "n":"_ .", "o":"_ _ _", "p":". _ _ .", "q":"_ _ . _", "r":". _ .", "s":". . .", "t":"_", "u":". . _", "v":". . . _", "w":". _ _", "x":"_ . . _", "y":"_ . _ _", "z":"_ _ . .", "1":". _ _ _ _", "2":". . _ _ _", "3":". . . _ _", "4":". . . . _", "5":". . . . .", "6":"_ . . . .", "7":"_ _ . . .", "8":"_ _ _ . .", "9":"_ _ _ _ .", "0":"_ _ _ _ _"}


print("Welcome to the text to morse code convertor.")
input = input("Please enter the word or the phrase: ")

output = ""
if " " in input:
    for word in input:
        for letter in word:
            if letter == " ":
                output += letter
            else:
                output += morse_code[letter]
            output += " | "
else:
    for letter in input:
        if letter == " ":
            output += letter
        else:
            output += morse_code[letter]
        output += " | "
print(output)