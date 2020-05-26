import sys
import string


argv = sys.argv
if (len(argv) != 3):
    print("ERROR")
    exit()
if (argv[1].isdigit() or not argv[2].isdigit()):
    print("ERROR")
    exit()

i = 0
phrase = argv[1]
len_need = int(argv[2])
words = phrase.split(" ")
ret = []
while (i < len(words)):
    word = words[i]
    if (len(word) > len_need):
        ret.append(word)
    i += 1
print(ret)
