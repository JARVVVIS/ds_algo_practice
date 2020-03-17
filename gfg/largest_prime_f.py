# Given a number N, the task is to find the largest prime factor of that number.
import math

def get_primes(num):
    ans = 0
    sqrt = int(math.sqrt(num))
    while not num%2:
        num=num//2
        ans=2
    for val in range(3,sqrt+1,2):
        while not num%val:
            num = num//val 
            ans=val
    if num>2:
        ans=int(num)
    return ans  


def main():
    t = int(input())
    for _ in range(t):
        num = int(input())  
        ans = get_primes(num)
        print(ans)


if __name__ == '__main__':
    main()
