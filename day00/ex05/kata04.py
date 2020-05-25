str = (0, 4, 132.42222, 10000, 12345.67)

print("day_%02d," % str[0], end=" ")
print("ex_%02d" % str[1], end=" ")
print(": %.2f," % str[2], end=" ")
print("%.2e," % str[3], end=" ")
print("%.2e" % str[4], end="")