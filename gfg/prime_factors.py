# Given a number N. The task is to print all its unique prime factors in increasing order.

def get_primes(num):
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val 
            primes.append(val)
        j=0
        while j<len(primes) and primes[j]*val<=num and primes[j]<=lp[val]:
            lp[primes[j]*val] = primes[j]
            j+=1
    return lp,primes

def main():
    MAX = int(1e6)
    lp,primes = get_primes(MAX)
    t = int(input())
    for _ in range(t):
        num = int(input())
        factors = []
        lpf = lp[num]
        factors.append(lpf)
        while num!=1:
            lpf = lp[num]
            if factors[-1]!=lpf:
                factors.append(lpf)
            num=num//lpf
        for f in factors:
            print(f,end=' ')
        print()

if __name__ == '__main__':
    main()