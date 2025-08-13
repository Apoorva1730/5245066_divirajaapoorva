#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #initialize counters for each type
    positive = 0
    negative = 0
    zero = 0
    
    total = len(arr) #total number of elements in the array
    
    #go through each num in the list
    for number in arr:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1
            
    #convert counts to required ratio format
    print("{0:.6f}".format(positive / total))
    print("{0:.6f}".format(negative / total))
    print("{0:.6f}".format(zero / total))
    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)