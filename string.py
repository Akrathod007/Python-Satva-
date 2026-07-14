s1 = "Ram"
s2 = """
    nwej
    wkenf
    klwen
    wekn
"""
"""
"""

# print(s1)
# print(s2)


"""
s =     M   i   s   s   i   s   s   i   p   p   i
+ =     0   1   2   3   4   5   6   7   8   9   10
- =    -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

s = "Mississippi"

print(s)
# print(s[0])
# print(s[6])
# print(s[-4])
# print(s[-1])
print("-----------------------------------------")


"""
s =     M   i   s   s   i   s   s   i   p   p   i
+ =     0   1   2   3   4   5   6   7   8   9   10
- =    -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
# 
"""
# s[start:stop:step] -> Slicing
# print(s[1:6])  # 1 to 5
# print(s[4:9])
# print(s[3:])
# print(s[:7])
# print(s[:])
# print(s[1:8:2])
# print(s[3:9:4])
# print(s[::5])
# print(s[::-1])
# print(s[-4:-9])
# print(s[-9:-4])
# print(s[8:1:-1])
# print(s[-4:-9:-1])
# print(s[3:-3])


print(len(s))

# using index :

# x = ""
# for i in range(0, len(s)):
#     print(i, "->", s[i])
#     x += s[i]

# for i in range(len(s) - 1, -1, -1):
#     print(i, "->", s[i])

# access direct character :

# for i in s:
#     print(i, end="")

# print(x)


# s = "Hello world"
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())


# x = chr(97)
# print(x)

# x = chr(34)
# print(x)

# y = ord("A")
# print(y)

# y = ord("$")
# print(y)

# y = ord("😊")
# print(y)

# x = chr(128522)
# print(x)


s = "Hi"

print(s.center(6, "$"))
print(s.ljust(6, "-"))
print(s.rjust(6, "-"))
print("42".zfill(10))

name = "Ram"
age = 21

print("Name is {} and age is {}".format(name, age))
print("Name is {} and age is {}".format(age, name))
print("Name is {name} and age is {age}".format_map({"name": name, "age": age}))
print(f"Name is {name} and age is {age}")
print(len("mississippi"))

print("My name is %s and I am %d years old." % (name, age))
# print("My name is %s and I am %d years old." % (age, name)) #Error

print("'Hello'")
print('"Hello"')
print("\\Hello\\")
print("\107")
print("\x4f")

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True (same object in memory)
print(a is c)  # False (different objects)

print("a" in "apple")
print("q" in "apple")
print("a" not in "apple")
print("q" not in "apple")
