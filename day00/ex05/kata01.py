languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

i = 0
keys = list(languages.keys())
values = list(languages.values())

while (i != len(keys)):
    print(keys[i], "was created by", values[i])
    i += 1
