## doing sieve in O(n)

def get_primes(num):
    lp  = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val ## yeh prime hai aur iska sabse chota divisor yahi hai
            primes.append(val)
        for j in primes:
            if val*j<=num:
                lp[val*j] = j
    return primes


def main():
    num = int(input())
    primes = get_primes(num)



if __name__ == '__main__':
    main()