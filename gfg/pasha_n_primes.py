import sys
def get_primes():
    num = int(1e6)
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val]=val
            primes.append(val)
        j=0
        while j<len(primes) and primes[j]<=lp[val] and val*primes[j]<=num:
            lp[val*primes[j]] = primes[j]
            j+=1
    del primes
    return lp


def main():
    primes = get_primes()
    t = int(input())
    for _ in range(t):
        A = sys.stdin.readline()
        print(A,type(A))
        N,Q = [int(x) for x in A.split()]
        arr = [int(primes[int(x)]==int(x)) for x in input().split()] ## O(1)
        for q in range(Q):
            a = sys.stdin.readline()
            l,r = [int(x) for x in a.split()]
            print(sum(arr[l-1:r]))


if __name__ == '__main__':
    main()

