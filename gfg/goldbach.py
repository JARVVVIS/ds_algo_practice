## return two primes a and b whose sum is equal to given even number


def get_primes(num):
    lp = [0]*(num+1) ## to store least prime divisors
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val ## least divisor of prime is the number itself (ignoring 1)
            primes.append(val)
        for j in primes:
            if val*j <= num:
                lp[j*val] = j ## all the multiples of these primes are not prime
    return primes,lp


def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        primes,lp = get_primes(num)
        for p in primes:
            q = num-p
            if lp[q]==q:
                print('{} {}'.format(p,q))
                break


if __name__ == '__main__':
    main()