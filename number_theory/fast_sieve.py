## doing sieve in O(n)

def get_primes(num):
    lp  = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val ## yeh prime hai aur iska sabse chota divisor yahi hai
            primes.append(val)
        j=0
        while j<len(primes) and val*primes[j]<=num and primes[j]<=lp[val]:
            lp[val*primes[j]] = primes[j]
            j+=1
    return primes

def main():
    num = int(input())
    primes = get_primes(num)
    print(primes)



if __name__ == '__main__':
    main()