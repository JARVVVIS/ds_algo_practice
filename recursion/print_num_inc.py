## Given n , print numbers from 1 to n recursively

def print_num(n):
    if n<=0:
        return 
    print_num(n-1)
    print(n,end=' ')


def main():
    n =  int(input())
    print_num(n)

if __name__ == '__main__':
    main()