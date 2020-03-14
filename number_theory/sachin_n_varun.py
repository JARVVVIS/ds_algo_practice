## Total number of combinations of a and b s.t. ax+by=d
## NOT DONE

def ext_euclid(a,b):
    if b>a:
        return ext_euclid(b,a)
    if b==0:
        return 1,0,a
    x1,y1,gcd = ext_euclid(b,a%b)
    x = y1
    y = x1-y1*(a//b)
    return gcd,x,y


def main():
    t = int(input())

    for _ in range(t):
        a,b,d = [int(x) for x in input().split()]
        _,y1,_ = ext_euclid(a,b)
        print(y1)
        k_max = (d//b-y1)//a
        ans = (k_max)+1
        print(ans)


if __name__ == '__main__':
    main()