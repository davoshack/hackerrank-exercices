import math
import os
import random
import re
import sys
import ipdb

def sockMerchant():
    n = 14
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    return sum([ar.count(i) // 2 for i in set(ar)])

if __name__ == '__main__':
    result = sockMerchant()
    print(result)

