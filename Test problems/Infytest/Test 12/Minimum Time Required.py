#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    low_bound = goal * min(machines) // len(machines)
    high_bound = goal * max(machines) // len(machines) + 1
 
    while low_bound < high_bound:
        days = (low_bound+high_bound) // 2
        produced = sum([days // machine for machine in machines])
        if produced >= goal:
            high_bound = days
        else:
            low_bound = days + 1
     
    return low_bound

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
