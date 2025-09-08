import sys

def fibonacci( n ) :
    if n < 2 :
        return n
    else :
        recurse1 = fibonacci( n - 1 )
        recurse2 = fibonacci( n - 2 )
        return recurse1 + recurse2

if __name__ == "__main__":
    print( fibonacci(int(sys.argv[1])) )
