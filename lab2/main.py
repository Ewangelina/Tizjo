#!/usr/bin/env python3

import sys

def invert(param, length):
    ret = ""
    for i in range(len(param)):
        if param[i].islower():
            ret = ret + param[i].upper()
        else:
            ret = ret + param[i].lower()
            
    while len(ret) < length:
        ret = ret + " "
    
    return ret

def is_number(x):
    return x.isnumerical()

def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string)):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(invert(param, -1),end="")
                skip = 1
            elif format_string[idx] == '#' and is_number(format_string[idx+1]):
                i = idx + 2
                num = int(format_string[idx+1])
                
                while is_number(format_string[i]):
                    num *= 10
                    num += int(format_string[i])
                    i += 1
                
                print(invert(param, num),end="")
                skip = idx - i
                
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
