# Given three numbers a, b and c such that a, b and c can be at most 1016. The task is to compute (a*b)%c



def main():
    t = int(input())
    for _ in range(t):
        a,b,c = [int(x) for x in input().split()]
        ans = ((a%c)*(b%c))%c
        print(ans)


if __name__ == '__main__':
    main()