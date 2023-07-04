import sys

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print('Sum: ', a + b)
        print('Diff: ', a - b)
        print('Product: ', a * b)
        print('Quotient: ', end='')
        try:
            print(a / b)
        except:
            print('ERROR (division by zero)')
        print('Remainder: ', end='')
        try:
            print(a % b)
        except:
            print('ERROR (modulo by zero)')
    except:
        print('AssertionError: wrong arguments')
elif len(sys.argv) == 1:
    print("""
    Usage: python operations.py <int1> <int2>
    Example:
        python operations.py 10 3
    """)
else:
    print('AssertionError: wrong arguments')
