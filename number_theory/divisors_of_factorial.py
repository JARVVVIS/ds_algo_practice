MODULO = 1e9+7

def get_sieve(num):
        sieve = [True]*(num+1) ## create an array to check primes
        for val in range(2,int((num)**1/2)+1):
                if sieve[val]: ## if the number is a prime 
                        for mul in range(val*val,num+1,val): ## set all the multiples to false
                                sieve[mul] = False
        primes = []
        for idx,val in enumerate(sieve):
                if val:
                        primes.append(idx)
        return primes[2:]


def get_divisors(num):
        global MODULO
        ans = 1
        primes = get_sieve(num) ## sieve to get primes smaller than num
        for prime in primes:
                ## calculate power for each prime
                k=1
                pow_sum=0
                power = pow(prime,k)
                while power<=num:
                        pow_sum += int(num/power)
                        k+=1
                        power = pow(prime,k)
                ans = ((ans%MODULO)*((pow_sum+1)%MODULO))%MODULO
        return ans


def main():
        t = int(input())
        for _ in range(t):
                num = int(input())
                ans = get_divisors(num)
                print(int(ans))

if __name__ == '__main__':
        main()