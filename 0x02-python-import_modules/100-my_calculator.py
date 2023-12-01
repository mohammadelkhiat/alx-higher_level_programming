#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    AC = len(sys.argv)
    if AC != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
   
    a = int(sys,argv[1])
    op = sys,argv[2]
    b = int(sys,argv[3])
    
    if op == "+":
        output = calc.add(a, b)
    elif op == "-":
        output = calc.sub(a, b)
    elif op == "/":
        output = calc.div(a, b)
    elif op == "*":
        output = calc.mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
        
    print("{} {} {} = {}".format(a, op,	b, output))
