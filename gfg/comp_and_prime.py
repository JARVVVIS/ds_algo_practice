# Given two integers L and R find the difference of number of composites and primes between the range L and R (both inclusive).

def get_primes():
    num = int(1e7)
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val 
            primes.append(val)
        j=0
        while j<=0 and primes[j]<=lp[val] and val*primes[j]<=num:
            lp[val*primes[j]] = primes[j]
            j+=1
    return primes


def main():
    primes = get_primes()
    t = int(input())
    for _ in range(t):
        a,b = [int(x) for x in input().split()]
        ans = 0
        for pr in primes:
            if pr<a:
                continue
            elif pr>b:
                break
            elif pr<=b and pr>=a:
                ans+=1
        val = (b-a+1)-ans
        print(val)





if __name__ == '__main__':
    main()