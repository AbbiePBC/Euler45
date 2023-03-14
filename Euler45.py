
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def main():
    
    n = 500
    while True:
        triangle_number = find_next_triangle_number(n)
        if is_pentagonal(triangle_number) and is_hexagonal(triangle_number):
            print(int(triangle_number))
            return
        n += 1

def find_next_triangle_number(n: int) -> int:
    return n*(n+1)*0.5

def is_pentagonal(triangle_number: int) -> bool:
    # n(3n−1)/2 = t
    # 3n^2 - n - 2t = 0
    # don't need to solve for n, just need discriminant to be >=0 and square
    # D = b^2 - 4ac.
    return real_integer_roots(a=3, b=-1, c=-2*triangle_number)
    

def is_hexagonal(triangle_number: int) -> bool:
    # Hn=n(2n−1)	
    # 2n^2 - n - t = 0
    return real_integer_roots(a=2, b=-1, c=-triangle_number)


def is_square(D: int) -> bool:
    # this relies on rounding, so not ideal solution
    root = D**0.5
    if int(root)**2 == D:
        return True
    return False

def real_integer_roots(a: int, b: int, c: int) -> bool:

    D:int = b**2 - 4*a*c
    if D < 0:
        return False
    elif not is_square(D):
        return False

    # b always == -1 and |b| < |D**0.5|, a always +ve => always want +ve D**0.5 value
    x = (-b + D**0.5) / (2*a)
    if int(x) == x:
        return True
    return False


if __name__ == '__main__':
    main()


