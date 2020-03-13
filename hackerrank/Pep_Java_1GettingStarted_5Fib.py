## Print nth fibonacci number

def main():
    n = int(input())
    if n==1 or n==0:
        print(n)
    else:
        vals = [0,1]
        while len(vals)<=n:
            num = sum(vals[-2:])
            vals.append(num)
        print(vals[-1])

if __name__ == '__main__':
    main()