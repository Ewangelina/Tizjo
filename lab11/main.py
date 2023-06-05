#!/usr/bin/env python3

import sys

def make_bin(x):
    return str(bin(x)).replace('0b', '')

def is_number(x):
    return x.isnumeric()

def do_print(input):
    ret = ""
    negative = ""
    if int(input) < 0:
        negative = "-"
        input = input[1:len(input)]
    
    letters = "abcdefghij"
    number = make_bin(int(input))
    done = len(number) - 1
    while done >= 0:
        for x in letters:
            if done < 0:
                break
            if number[done] == '1':
                ret = x + ret
            else:
                ret = '0' + ret     
            done -=1

    return negative + ret


def my_printf(format_string,param):
    #print(int("1.1"))
    skip = 0
    for idx in range(0,len(format_string) - 1):
        if skip == 0:
            if format_string[idx] == '#' and format_string[idx+1] == 'b':
                try:
                    print(do_print(param),end="")
                    skip = 1 
                except Exception as a:
                    print(a)
                    print(format_string[idx],end="") 
                
            else:
                print(format_string[idx],end="")
        else:
            skip -= 1
    if (skip == 0):
        print(format_string[len(format_string) - 1],end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
