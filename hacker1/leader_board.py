import math
import os
import random
import re
import sys

def climbingLeaderboard(a, b):
    # Write your code here
    a=sorted(list(set(a)),reverse=True)
    print(a)
    b.sort(reverse=True)
    print(b)
    l=len(a)
    j=0
    r1=[]
    for i in range(len(b)):
        while j<l and b[i]<a[j]:
            j+=1
        r1.append(j+1)
    return r1[::-1]
if __name__ == '__main__':
    #ranked = list(map(int, input().rstrip().split()))
    #player_count = int(input().strip())
    #player = list(map(int, input().rstrip().split()))
    ranked=[100,90,90,80]
    player=[70,80,105]
    result = climbingLeaderboard(ranked, player)
    print(result)
