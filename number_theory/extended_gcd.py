## find the GCD and x and y of two numbers a and b s.t. ax+by = gcd(a,b)

def get_gcd(a,b):
    if b>a:
        return get_gcd(b,a)
    if b==0:
        return (a,1,0)
    gcd,x1,y1 = get_gcd(b,a%b)
    x = y1 
    y = x1 - y1*(int(a/b))
    return (gcd,x,y)


def main():
    ## Take the numbers as input
    a = int(input())
    b = int(input())

    gcd,x,y = get_gcd(a,b)
    print('{}*{} + {}*{} = {}'.format(a,x,b,y,gcd))


if __name__ == '__main__':
    main()