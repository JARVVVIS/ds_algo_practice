## given a number N print least prime factor of all numbers from 1 to N


def get_prime_factors(num):
    lp = [0]*(num+1) ## array to store least prime factor of all numbers
    lp[1] = 1
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val ## a number number is it's own least factor
            primes.append(val)
        for j in primes:
            if j*val<=num:
                lp[j*val] = j
    return lp,primes


def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        lp,primes = get_prime_factors(num)
        for val in lp[1:]:
            print(val,end=' ')
        print()
    

if __name__ == '__main__':
    main()