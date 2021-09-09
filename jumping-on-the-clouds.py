#!/bin/python3

import math
import os
import random
import re
import sys
import ipdb

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds():
    i = 0
    j = 0
    c = [0,0,0,1,0,0]
    while i < len(c) - 1:
        ipdb.set_trace()
        if (len(c)-1) - i > 1:
            if c[i+2] != 1:
                i += 2
        elif c[i+1] != 1:
            i += 1
        j += 1
    return j

if __name__ == '__main__':

    result = jumpingOnClouds()
    print(result)



