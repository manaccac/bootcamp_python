import string

def text_analyzer(text):
    upper = 0
    lower = 0
    punc = 0
    space = 0
    i = len(text) - 1
    nb_chara = i
    if (i == 0):
        print ("What is the text to analyse")
        exit()
    while (i >= 0):
        if (text[i].isupper()):
            upper += 1
        elif (text[i].islower()):
            lower += 1
        elif (text[i].isspace()):
            space += 1
        elif (text[i] in string.punctuation):
            punc += 1
        i = i - 1
    print ("The text contains", nb_chara, " characters:\n")
    print("- ", upper, " upper letters")
    print("- ", lower, " lower letters")
    print("- ", punc, " punctuation marks")
    print("- ", space, " spaces")
    return