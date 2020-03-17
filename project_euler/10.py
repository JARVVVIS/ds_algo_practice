## Sum of all primes below 2 million


def get_sum(num,lim):
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val 
            if val>lim:
                return sum(primes)
            primes.append(val)
        j=0
        while j<len(primes) and primes[j]<=lp[val] and val*primes[j]<=num:
            lp[primes[j]*val] = primes[j]
            j+=1






def main():
    MAX = int(1e8)
    lim = int(input())
    ans = get_sum(MAX,lim)
    print(ans)



if __name__ == '__main__':
    main()