# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: manaccac <manaccac@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/25 09:19:14 by manaccac          #+#    #+#              #
#    Updated: 2020/05/25 09:22:29 by manaccac         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys

argc = len(sys.argv)
if (argc == 1):
    exit()
if (argc > 2):
    print("ERROR")
    exit()
nb = sys.argv[1]
if (nb.isdigit()):
    nb = int(nb)
    if (nb == 0):
        print ("I'm Zero.")
        exit()
    if (nb % 2 == 0):
        print ("I'm Even.")
        exit()
    else:
        print ("I'm Odd.")
        exit()
else:
    print ("ERROR")
    exit()