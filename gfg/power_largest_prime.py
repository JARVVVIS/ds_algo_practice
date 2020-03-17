# You are given a number 'n'. Your task is to check whether the power of its 
# largest prime factor is greater than one or not.
# Print "YES" if the power is greater than one otherwise print "NO";
import math


def get_largest(num):
    ans=0
    while not num%2:
        num=num//2
        ans=2
    sqrt = math.sqrt(num)
    for val in range(3,sqrt+1,2):
        if not num%val:
            ans=val
            num = num//val 
    if num>2:
        ans=num 
    return ans


