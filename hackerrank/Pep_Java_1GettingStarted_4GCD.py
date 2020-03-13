## return gcd of two numbers 
def gcd(x,y):
    if y>x:
        return gcd(y,x)
    if y == 0:
        return x
    return gcd(y,x%y)


def main():
    x = int(input())
    y = int(input())
    ans = gcd(x,y)
    print(ans)

if __name__ == '__main__':
    main()