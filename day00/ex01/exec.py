# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: manaccac <manaccac@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 08:44:39 by manaccac          #+#    #+#              #
#    Updated: 2020/05/25 08:44:41 by manaccac         ###   ########lyon.fr    #
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