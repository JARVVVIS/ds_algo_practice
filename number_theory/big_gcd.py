## Find gcd of two numbers when one number is of order 10^250


def big_modulo(a,b):
    small_mod = 0
    for val in b:
        big_mod = ((10*small_mod)%a+int(val)%a)%a
        small_mod = big_mod
    return big_mod


def get_gcd(a,b):
    if b==0:
        return a 
    return get_gcd(b,a%b)


def main():
    t = int(input())
    for _ in range(t):
        a,b = input().split()
        a = int(a)
        if a==0:
            print(b)
        else:
            b_mod_a = big_modulo(a,b) ## calculate b%a
            gcd = get_gcd(a,b_mod_a)
            print(gcd)


if __name__ == '__main__':
    main()