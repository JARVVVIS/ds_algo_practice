# Given a number N. Find if it can be expressed as sum of two prime numbers.

def check_prime(num):
    if num==1:
        return False
    for val in range(2,num):
        if not num%val:
            return False
    return True


def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        if num==2 or num==1:
            print('No')
        elif not num%2:
            print('Yes')
        else:
            m = num-2
            prime = check_prime(m)
            if prime:
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    main()