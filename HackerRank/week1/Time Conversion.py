#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #extract parts of the time string
    period = s[-2:] #AM or PM
    hour = int(s[:2]) #first two characters are the hour
    rest = s[2:-2] #the reset (":mm:ss")
    
    #convert hour based on AM/PM rules
    if period == "AM":
        if hour == 12:
            hour = 0 #midnight case
    else: #PM case
        if hour != 12:
            hour += 12 #afternoon/evening case
            
    #format the hour to always be two digits
    return "{:02d}{}".format(hour, rest)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
