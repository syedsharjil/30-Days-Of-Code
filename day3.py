import math
import os
import random
import re
import sys
def weird(N1):
    # function to check all the given cases
    if(N1%2!=0):
        print("Weird")
    else:
        if(N1>=2 and N1<=5):
            print("Not Weird")
        if(N1>=6 and N1<=20):
            print("Weird")
        if(N1>20):
            print("Not Weird")




if __name__ == '__main__':
    N = int(input())
    weird(N)
