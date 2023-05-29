#!/usr/bin/env python3

import sys

def make_hex(x):
    h = str(hex(x))
    ret = ""
    for i in range(2, len(h)):
        ret += h[i]
    
    return ret

def is_number(x):
    return x.isnumeric()

def no_digits(x):
    ret = 0
    for i in range(0, len(x)):
        if is_number(x[i]):
            ret += 1

def getF(input):
    o = int(input)
    n = no_digits(input)
    return int((o*2)/n))

def do_print(input):
    f = getF(input)
    if f % 2 == 0:
        return str(f)
    else:
        return make_hex(f)

        
def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string) - 1):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == 'a':
                try:
                    print(getF(param),end="")
                    skip = 1  
                except:
                    print(format_string[idx],end="")
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
