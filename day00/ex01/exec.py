# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: manaccac <manaccac@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/24 10:47:34 by manaccac          #+#    #+#              #
#    Updated: 2020/05/24 12:29:02 by manaccac         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys

argc = len(sys.argv)
i = argc - 1
while (i != 0):
    str = sys.argv[i]
    str_len = len(str)
    res = str[::-1]
    res = res.swapcase()
    i = i - 1
    if (i == 0):
        print (res, end='')
    else:
        print (res, end=' ')