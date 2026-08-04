"""s1 = {1, 2, 3, 4, 5}
print(s1)
print(type(s1))

s2 = {}
print(type(s2))

s3 = set()
print(type(s3))
print(len(s3))

s4 = {1, 2, 3, 2, 3, 4, 5, 4, 5, 6}
print(s4)

s5 = set([1, 2, 3, 4, 5, 4, 5])
print(s5)

# print(s5[0])  # Error

s6 = {"Hello", "Hi", "Bye", "apple"}
print(s6)

s7 = {(1, 2, 3), (4, 5, 6)}
print(s7)

# s8 = {[1, 2, 3]}
# print(s8)

"""

"""
s1 = {1, 2, 3, 4, 5, 6}
print(s1)
s1.add(7)
print(s1)

# s2 = {1, 2, 1.2, 3.4, "Hello", "hi"}
# print(s2)

s1.remove(4)
# s1.remove(44)
print(s1)

# s1.discard(2)
s1.discard(22)
print(s1)

elm = s1.pop()
print(elm)
print(s1)

elm = s1.pop()
print(elm)
print(s1)


s2 = {"Hello", "Hi", "Bye", "Good", "Bad"}
print(s2)
elm = s2.pop()
print(elm)
print(s2)


s2.clear()
print(s2)

"""


# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}

# print(s1.union(s2))
# print(s1 | s2)

# print("-----------------------------------")
# print(s1.intersection(s2))
# print(s1 & s2)

# print("-----------------------------------")

# print(s1.difference(s2))
# print(s1 - s2)
# print(s2 - s1)

# print("-----------------------------------")
# print(s1.symmetric_difference(s2))
# print(s2 ^ s1)


# print("-----------------------------------")

# a = {1, 2}
# b = {1, 2, 3}
# c = {4, 5}
# print(a <= b)
# print(a.issubset(b))
# print(b.issubset(a))
# print(b >= a)
# print(b.issuperset(a))
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# print("-----------------------------------")

x = {1, 2}
y = {2, 3}

# x.update(y)
# print(x)

# x.intersection_update(y)
# print(x)

# x.difference_update(y)
# print(x)

# x.symmetric_difference_update(y)
# print(x)

s = frozenset([1, 2, 3, 4])
print(s)
print(type(s))
# s.add(10)


s1 = {1, 2, 3, 4, 5, 6, 7}

for i in s1:
    print(i)


# for i in range(len(s1)):
#     print(i, "->", s1[i])

s2 = {"Hello", "Bye", "Good", "Namaste"}
for i in s2:
    print(i)
