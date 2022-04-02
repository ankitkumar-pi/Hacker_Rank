#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    print(f'hello {s}')
    
    ls = []
    for i in s:
        ls.append(ord(i))    
    reverse_string = s[::-1]
    
    ls_nxt = []
    for i in reverse_string:
        ls_nxt.append(ord(i))

        
    or_list_ls = []
    or_list_rv = []
    for i in range(len(ls)):
        try:
            diff = ls[i+1] - ls[i]
            or_list_ls.append(abs(diff))
            
            diff_2 = ls_nxt[i+1] - ls_nxt[i]
            or_list_rv.append(abs(diff_2))
        except:
            pass
            
    
    if or_list_ls == or_list_rv:
        return 'Funny'
    else:
        return 'Not Funny'

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
