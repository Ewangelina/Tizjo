#!/usr/bin/env python3

import sys

def shiftHex(x):
    if x == 'a':
        return 'g'
    elif x == 'b':
        return 'h'
    elif x == 'c':
        return 'i'
    elif x == 'd':
        return 'j'
    elif x == 'e':
        return 'k'
    elif x == 'f':
        return 'l'
    else:
        return x

def hexadecimal(param):
    new_param = hex(int(param))
    ret = ""
    
    for i in range(2,len(new_param)):
        ret += 
    return param


def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string)):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                print(hexadecimal(param),end="")
                skip = 1
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
