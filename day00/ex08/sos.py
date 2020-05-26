import sys


MORSE_CODE_DICT = {
                    'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


argc = len(sys.argv)

if(argc == 1):
    exit()
words = []
i = 1

while (i < len(sys.argv)):
    word = sys.argv[i]
    words += word.split()
    i += 1

i = 0
while (i != len(words)):
    word = words[i]
    if (not word.isalnum()):
        print("ERROR")
        exit()
    i += 1
i = 0
c = ''
while (i != len(words)):
    word = words[i].upper()
    j = 0
    while (j != len(word)):
        c = word[j]
        print(MORSE_CODE_DICT[c], end=" ")
        j += 1
    i += 1
    if (i != len(words)):
        print("/ ", end="")
