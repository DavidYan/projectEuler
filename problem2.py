"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

def nthFibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return nthFibonacci(num-1) + nthFibonacci(num-2)

def main():
    current = 1
    sum = 0
    while True:
        fib = nthFibonacci(current)
        
        # Check if we've gone too far
        if fib > 4000000:
            print sum
            return
        
        # Else check if we can add to sum
        if fib % 2 == 0:
            sum += fib

        current += 1

if __name__ == "__main__":
    main()
