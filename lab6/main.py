#!/usr/bin/env python3

import sys

def is_number(x):
    return x.isnumeric()
    
    
def number_change(x):
    if is_number(x):
        num = int(x)
        return str((((num * 9) + 1) % 10))
    else:
        return x





def invert_numbers_len(param, length, filler):
    ret = ""
    nums = ""
    skip = 0
    
    for i in range(len(param)):
        while is_number(param[i + skip]):
            nums = nums + number_change(param[i + skip])
            skip += 1
            if i + skip >= len(param):
                ret = ret + nums
                while len(ret) < length:
                    if param[0] == "-":
                        length += 1
                    if (param[0] == "-" and filler != " "):
                        ret = ret[0] + filler + ret[1:len(ret)]
                    else:
                        ret = filler + ret
                return ret
            
        if nums != "":
            ret = ret + nums
            nums = ""
            
        if skip == 0:
            ret = ret + param[i]
        else:
            skip -= 1
                	
    if param[0] == "-":
            length += 1
            
    while len(ret) < length:
        if (param[0] == "-" and filler != " "):
            ret = ret[0] + filler + ret[1:len(ret)]
        else:
            ret = filler + ret
        
    return ret


def my_printf(format_string,param):
    #print(format_string)
    skip = 0
    for idx in range(0,len(format_string)):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and is_number(format_string[idx+2]): # #.5g
                i = idx + 3
                num = int(format_string[idx+2])
                filler = " "
                if num == 0:
                    filler = "0"
                
                while is_number(format_string[i]):
                    num *= 10
                    num += int(format_string[i])
                    i += 1
                
                if format_string[i] == 'g':
                    print(invert_numbers_len(param, num, filler),end="")
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
