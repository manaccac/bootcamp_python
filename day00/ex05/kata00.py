t = (19, 42, 21)

length = len(t)
print("The", length, "numbers are: ", end='')
count =0;
for i in t:
    print(i, end='')
    if count != length -1:
        print(", ", end="")
    count += 1