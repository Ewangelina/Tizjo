#!/usr/bin/env python3

import sys

def invert(param):
    ret = ""
    for i in range(len(param)):
        if param[i].islower():
            ret = ret + param[i].upper()
        else:
            ret = ret + param[i].lower()
    
    return ret


def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(invert(param),end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
