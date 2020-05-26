import sys


argc = len(sys.argv)
i = argc - 1
if (argc > 2):
    while (i != 0):
        str = sys.argv[i]
        str_len = len(str)
        res = str[::-1]
        res = res.swapcase()
        i = i - 1
        if (i == 0):
            print(res, end='')
        else:
            print(res, end=' ')
