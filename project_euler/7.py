## Find the 10001st prime


def get_primes(num,pr):
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if len(primes)==pr:
            return primes[-1]
        if not lp[val]:
            lp[val] = val 
            primes.append(val)
        j=0
        while j<len(primes) and primes[j]*val<=num and primes[j]<=lp[val]:
            lp[primes[j]*val] = primes[j]
            j+=1



def main():
    num = int(1e8)
    pr = int(input())
    ans = get_primes(num,pr)
    print(ans)

if __name__ == '__main__':
    main()