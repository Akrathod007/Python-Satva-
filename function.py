"""
Function : It is block of code that perform specific Task and can reuse anywhere in the program.

Types of Function:

1) Built - in function

2) User Defined Function : Make by developer or programmer

Types of User Defined Function :

1) No Return Type and No Arguments
2) No Return Type and With Arguments
3) With Return Type and No Arguments
4) With Return Type and With Arguments
"""

# 1) No Return Type and No Arguments


def sayHello():
    print("Hii")
    print("Hello")


sayHello()
sayHello()
sayHello()

print("---------------------------------------")

# 2) No Return Type and With Arguments


def add(a, b):
    print(f"{a} + {b} = {a + b}")


add(10, 20)
add(30, 50)
add(19, 25)

print("---------------------------------------")


# 3) With Return Type and No Arguments
def fact():
    no = int(input("Enter a number : "))
    f = 1
    for i in range(1, no + 1):
        f = f * i

    return f


x = fact()
print(x)
print(fact())


# 4) With Return Type and With Arguments


def isPrime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f = f + 1

    if f == 2:
        return 1
    else:
        return 0


isP = isPrime(12)

if isP == 1:
    print("Prime")
else:
    print("Not Prime")
