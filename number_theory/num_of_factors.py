# A number is called n-factorful if it has exactly n distinct prime factors
# . Given positive integers a, b, and n, your task is to find the number of 
# integers between a and b, inclusive, 
# that are n-factorful. We consider 1 to be 0-factorful.


def get_factors(a,b):
    sieve = [True]*(b+1)
    factors = {val:0 for val in range(b+1)}

    factors[2] = 1
    for mul in range(2*2,b+1,2):
        sieve[mul] = False
        factors[mul] += 1

    for val in range(3,b+1,2):
        if sieve[val]:
            factors[val] = 1
            for mul in range(val*2,b+1,val):
                sieve[mul] = False
                factors[mul] += 1
    return factors


def main():
    a,b = 1,1000000
    factors = get_factors(a,b)
    ans = {val:[0]*(1+b) for val in range(0,11)}
    for num_fac in ans:
        ans[num_fac][1] = 0
        for val in range(a,b+1):
            ans[num_fac][val] += ans[num_fac][val-1] + int(factors[val] == num_fac)
    t = int(input())
    for _ in range(t):
        a,b,n = [int(x) for x in input().split()]
        if n ==0:
            print('1')
        else:
            x,y = ans[n][a-1],ans[n][b]
            rng = y-x
            print(rng)


if __name__ == '__main__':
    main()