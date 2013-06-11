
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    n = int(raw_input('Enter a number:'))
    for i in range(0, n+1):
        print fib(i)
