# Given a number N. The task is to print all its unique prime factors in increasing order.

def get_primes(num):
    sieve = [True]*(num+1)  
    factors = []
    for val in range(2,num+1):
        if sieve[val]:
            if val==num:
                factors = [val]
                return factors
            for mul in range(2*val,num+1,val):
                sieve[mul] = False
                if mul == num:
                    factors.append(val)
    return factors

def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        factors = get_primes(num)
        for f in factors:
            print(f,end=' ')
        print()


if __name__ == '__main__':
    main()