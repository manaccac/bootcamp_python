import sys
import math


def error(i):
    if (i == 1):
        print("InputError: too many arguments\n")
    elif (i == 2):
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")


argc = len(sys.argv)
i = argc - 1
if (argc > 3):
    error(1)
    exit()
if (argc < 3):
    error(0)
    exit()
nb1 = sys.argv[1]
nb2 = sys.argv[2]
if (nb1.isdigit()):
    nb1 = int(nb1)
else:
    error(2)
    exit()
if (nb2.isdigit()):
    nb2 = int(nb2)
else:
    error(2)
    exit()
print("Sum:       \t", nb1 + nb2)
print("Difference:\t", nb1 - nb2)
print("Product:   \t", nb1 * nb2)
if (nb2 == 0):
    print("Quotient:   \t ERROR (div by zero)")
    print("Remainder:  \t ERROR (modulo by zero)")
    exit()
print("Quotient:  \t", nb1 / nb2)
print("Remainder: \t", nb1 % nb2)
