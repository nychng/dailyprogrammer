def factorial(n):
    '''
    Calculates the factorial of a given number
    e.g 5: 5 * 4 * 3 * 2 * 1
    '''
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

if __name__ == '__main__':
    selection = raw_input('Enter a number:')
    print 'The factorial of %s is %s' % (selection, factorial(int(selection)))
