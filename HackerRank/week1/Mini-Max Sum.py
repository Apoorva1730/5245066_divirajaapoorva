#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #sort the array to amke it easy to find min and max 4-element sums
    arr.sort()
    
    #the minimum sum is the sum of the first 4 (smallest) numbers
    min_sum = sum(arr[:4])
    
    #the maximum sum is the sum of the last 4 (largest) numbers
    max_sum = sum(arr[1:])
    
    #print both values in one line, separated by a space
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
