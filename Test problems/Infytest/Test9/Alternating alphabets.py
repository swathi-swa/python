#!/bin/python3

import math
import os
import random
import re
import sys
k=int(input())
for i in range(0,k):
    s=str(input())
    v=0
    n=[]
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            n.append(s)
            v+=1
    print(v)
    
