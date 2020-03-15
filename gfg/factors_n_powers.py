# Given a number N, print all its unique prime factors and their powers in N.
def get_primes(num):
    sieve = [True]*(num+1)
    factors = {val:[] for val in range(num+1)}
    for val in range(2,num+1):
        if sieve[val]:
            factors[val] = [val]
            for mul in range(2*val,num+1,val):
                sieve[mul] = False
                factors[mul].extend([val])
    return factors

def get_power(num,factors):
    powers = []
    for prime in factors:
        power = 0
        while not num%prime:
            num=num/prime
            power += 1
        powers.append(power)
    return powers


def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        factors = get_primes(num)
        factors_n = factors[num]
        powers = get_power(num,factors_n)
        for factor,power in zip(factors_n,powers):
            print(factor,power,end=' ')
        print()


if __name__ == '__main__':
    main()