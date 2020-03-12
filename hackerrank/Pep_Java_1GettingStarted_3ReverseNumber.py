# Take as input n. Print the number in reverse.


def main():
    num = input() ## take input as a string
    ans = ''
    for rev in reversed(num):
        ans+= rev
    print(ans)

if __name__ == '__main__':
    main()