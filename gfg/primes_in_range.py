def get_prime(a,b):
    sieve = [True]*(b+1)
    sqrt = int(b**1/2)
    for val in range(2,sqrt+1):
        if sieve[val]:
            for mul in range(val*val,b+1,val):
                sieve[mul] = False
    return sieve


def main():
    t = int(input())
    for _ in range(t):
        a,b = [int(x) for x in input().split()]
        primes = get_prime(a,b)
        for idx,prime in enumerate(primes):
            if prime and idx>=a and idx!=1:
                print(idx,end=' ')
        print()




if __name__ == '__main__':
    main()