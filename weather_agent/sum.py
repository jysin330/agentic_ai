from __future__ import print_function

# this function takes two arguments: a and b
def sum(a, b):
    result = a + b
    return result

if __name__ == '__main__':
    a = float(input("Enter a number:" ))
    b = float(input("Enter another number: "))
    print(f"The sum of the two numbers is: , {sum(a, b)}")
