## Find Largest Prime Factor in O(root(N))
import math

def get_prime(num):
    max_prime = 0

    while not num%2:
        num=num//2
        max_prime = 2
    sqrt = int(math.sqrt(num))
    for val in range(3,sqrt+1,2):

        while not num%val:
            num=num//val 
            max_prime = val

    if num>2:
        max_prime = num 

    return max_prime



def main():
    num = int(input())
    max_prime = get_prime(num)
    print(max_prime)

if __name__ == '__main__':
    main()