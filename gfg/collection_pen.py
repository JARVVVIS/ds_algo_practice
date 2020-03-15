# Everyone have some habits to collect one thing or the other. 
# Harshit also has the craze to collect pens but in 3 piles. In first pile, 
# he collected A pens and in the second pile, he collected B pens but in the third and 
# the last pile , he think of something different. He decided to collect only the minimum 
# number of pens in third pile so that the sum of pens in the three piles will give him a 
# prime number. Note: there should be atleast one pen in the third pile.

def get_primes(num=3000):
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val
            primes.append(val)
        for j in primes:
            if j*val<= num:
                lp[j*val] = j  
    return primes

def main():
    t = int(input())
    for _ in range(t):
        a,b = [int(x) for x in input().split()]
        primes = get_primes()
        for prime in primes:
            if prime>a+b:
                c = prime-(a+b)
                break
        print(c)


if __name__ == '__main__':
    main()