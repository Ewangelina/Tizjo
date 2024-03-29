#!/usr/bin/env python3

import sys

def is_number(x):
    return x.isnumeric()

def invert_numbers(param):
    ret = ""
    nums = ""
    skip = 0
    
    for i in range(len(param)):
        while is_number(param[i + skip]):
            nums = param[i + skip] + nums
            skip += 1
            if i + skip >= len(param):
                return ret + nums
            
        if nums != "":
            ret = ret + nums
            nums = ""
            
        if skip == 0:
            ret = ret + param[i]
        else:
            skip -= 1
    return ret

def invert_lengthen(param, min_length):
    ret = ""
    for i in range(len(param)):
        if param[i].islower():
            ret = ret + param[i].upper()
        else:
            ret = ret + param[i].lower()
            
    while len(ret) < min_length:
        ret = " " + ret
    
    return ret

def invert_shorten(param, max_length):
    ret = ""
    for i in range(max_length):
    	if i > len(param):
            break
            
    	if param[i].islower():
            ret = ret + param[i].upper()
    	else:
            ret = ret + param[i].lower()
                
    return ret



def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string)):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == 'g' and param.isnumeric():
                print(invert_numbers(param),end="")
                skip = 1
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
