## Print all fibonacci numbers <=n

def main():
    n = int(input())
    vals = [0,1]
    while vals[-1]<=n:
        num = sum(vals[-2:])
        vals.append(num)
    [print(x,end=' ') for x in vals[:-1]]

if __name__ == '__main__':
    main()