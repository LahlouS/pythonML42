import sys

if len(sys.argv) == 2:
    try:
        integer = int(sys.argv[1])
        if not integer:
            print("I'm zero")
        elif integer % 2 == 0:
            print("I'm even")
        else:
            print("I'm odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
