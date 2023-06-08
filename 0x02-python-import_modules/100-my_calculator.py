#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        allowed_optr = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(allowed_optr.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.ext(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print[("{} {} {} = {}".format(a, sys.argv[2], b,
        allowed_optr[sys.argv[2]](a, b)))]
