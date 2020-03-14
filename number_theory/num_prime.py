## Given a number N, find number of primes in range [1,N]

def get_primes(num):
    sieve = [True]*(num+1) ## create an array to check primes
    for val in range(2,int((num)**1/2)+1):
        if sieve[val]: ## if the number is a prime 
            for mul in range(val*val,num+1,val): ## set all the multiples to false
                sieve[mul] = False
    return sieve

def main():
    num = int(input())
    sieve = get_primes(num)
    ans = sum([int(x) for x in sieve])-2
    print(ans)

if __name__ == '__main__':
    main()