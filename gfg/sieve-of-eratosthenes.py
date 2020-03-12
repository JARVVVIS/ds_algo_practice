# Take as input n. Determine all prime numbers till n and print them on the same line with 
# spaces in between


def s_update(n=2):
    sieve = [True]*(n+1) ## create a n+1 array
    sqrt_n  =  int((n)**1/2)
    for num in range(2,sqrt_n):
        if sieve[num]:
            for mul in range(num*num,n+1,num):
                sieve[mul] = False ## all multiples of num set to False
    return sieve


def s_print(sieve):
    for idx,val in enumerate(sieve):
        if val and idx>1:
            print(idx,end=' ')


def main():
    t = int(input()) ## number of test cases

    for _ in range(t):
        n  = int(input())
        sieve = s_update(n)
        s_print(sieve)
        print()


if __name__ == '__main__':
    main()