# for loop

"""
for variable in sequaence
    //code
"""

# for i in range(1, 11):
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(1, 11, 4):
#     print(i)


# for i in range(10, -1, -1):
#     print(i)

# sum : 1 to 10
# mul : 1 to 10
# esum and osum

# fibonacci series : 1 1 2 3 5 8 13
"""
                     a b
                    a  = 1
                    b =  1
                    c = a + b
                    a = b
                    b = c
                    
"""


# a = 1
# b = 1

# no = int(input("Enter a series number : "))
# print(a)
# print(b)
# for i in range(3, no + 1):
#     c = a + b
#     print(c)
#     a = b
#     b = c


# print("Hello", end=" ")
# print("World", end="@")
# print("Bye")

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

# x = ord("A")
# print(x)
# y = chr(97)
# print(y)

# for i in range(1, 6):
#     for j in range(1, 4):
#         print("i :", i, "j :", j)

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

A B C D E
A B C D E
A B C D E
A B C D E
A B C D E


*
* *
* * *
* * * *
* * * * *


1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

A
A B
A B C
A B C D
A B C D E

A
B B
C C C
D D D D
E E E E E

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

1
A B
1 2 3
A B C D
1 2 3 4 5

* * * * *
*       *
*       *
*       *
* * * * *

    *
    *
* * * * *
    *
    *
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
#     print()


# for i in range(1, 11):
#     # if i == 5:
#     #     break
#     if i == 5:
#         continue
#     print(i)

# code


# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1


# sum = 0

# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i + 1

# print("Sum :", sum)


# no = int(input("Enter a number : "))

# i = 1
# while i <= 10:
#     print(no, "*", i, "=", no * i)
#     i = i + 1


"""
1.factorial of no
2.prime number
3.find factors of numbers
"""

"""
no = 1234 -> 4
no = 12 -> 2

no = 1234 // 10 -> 123 -> dc -> 1
no = 123 // 10 -> 12 -> dc -> 2
no = 12 // 10 -> 1 -> dc -> 3
no = 1 // 10 -> 0 -> dc -> 4
"""

no = int(input("Enter a number : "))

dc = 0
sum = 0
while no != 0:
    d = no % 10
    sum = sum + d
    dc = dc + 1
    no = no // 10

print("Digit Count is", dc)
print("Digit Sum is", sum)


"""
145 -> 1! + 4! + 5! -> 1 + 24 + 120 -> 145
"""
