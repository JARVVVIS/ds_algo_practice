## Check if a number is present in the array or not


def check(arr,x):
    if x == arr[0]:
        return True
    if len(arr)==1:
        return False
    return check(arr[1:],x)



def main():
    size = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())
    ans  = check(arr,x)
    if ans:
        print('true')
    else:
        print('false')


if __name__ == '__main__':
    main()