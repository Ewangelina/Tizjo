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
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(invert_lengthen(param, -1),end="")
                skip = 1
            elif format_string[idx] == '#' and format_string[idx+1] == 'g':
                print(invert_numbers(param),end="")
                skip = 1
            elif format_string[idx] == '#' and is_number(format_string[idx+1]): # #5k i #5.5k
                i = idx + 2
                num = int(format_string[idx+1])
                
                while is_number(format_string[i]):
                    num *= 10
                    num += int(format_string[i])
                    i += 1
                
                if format_string[i] == 'k':
                    print(invert_lengthen(param, num),end="")
                    skip = i - idx
                elif format_string[i] == '.' and is_number(format_string[i + 1]):
                    short_num = int(format_string[i+1])
                    i += 2
                    
                    while is_number(format_string[i]):
                    	short_num *= 10
                    	short_num += int(format_string[i])
                    	i += 1
                    
                    if format_string[i] == 'k':
                    	print(invert_lengthen(invert_shorten(invert_lengthen(param, 0), short_num), num), end="")
                    	skip = i - idx
                    else:
                    	print(format_string[idx],end="")
                else:
                    print(format_string[idx],end="")
            elif format_string[idx] == '#' and format_string[idx+1] == '.': # #.5k
                i = idx + 2
                num = 0
                
                while is_number(format_string[i]):
                    num *= 10
                    num += int(format_string[i])
                    i += 1
                
                if format_string[i] == 'k' and i > idx + 2:
                    print(invert_shorten(param, num),end="")
                    skip = i - idx
                else:
                    print(format_string[idx],end="")
                
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
