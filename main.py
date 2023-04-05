morse_code = {
"A": ".-",
"B": "-...",
"C": "-.-.",
"D": "-..",
"E": ".",
"F": "..-.",
"G": "--.",
"H": "....",
"I": "..",
"J": ".---",
"K": "-.-",
"L": ".-..",
"M": "--",
"N": "-.",
"O": "---",
"P": ".--.",
"Q": "--.-",
"R": ".-.",
"S": "...",
"T": "-",
"U": "..-",
"V": "...-",
"W": ".--",
"X": "-..-",
"Y": "-.--",
"Z": "--..",
"0": "-----",
"1": ".----",
"2": "..---",
"3": "...--",
"4": "....-",
"5": ".....",
"6": "-....",
"7": "--...",
"8": "---..",
"9": "----.",
".": ".-.-.-",
",": "--..--",
"?": "..--..",
"=": "-...-",
}

sentence = input("What sentence would you like translated into Morse Code?").upper()
print(sentence)

morse_sentence = []

for letter in sentence:
    if letter in morse_code:
        x = morse_code.get(letter)
        morse_sentence.append(x)

print(' '.join(morse_sentence))