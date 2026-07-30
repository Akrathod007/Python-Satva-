"""t1 = (10, 20, 30, 40, 50)
print(t1)
print(type(t1))

t2 = (1, 3.14, "Hello", True)
print(t2)

t3 = ()
print(t3)

t4 = 1, 2, 3, 4, 5
print(t4)

print(t4[0])  # First element
print(t4[-1])  # Last element

print(t4[1:4])  # From index 1 to 3
print(t4[:3])  # First 3 elements
print(t4[-3:])  # Last 3 elements

t5 = (10,)
print(t5)


t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result)

t = (10, 20)
print(t * 3)

t = (1, 2, 3, 4)
print(2 in t)  # True
print(5 not in t)  # True

print(len(t))
print(sum(t))
print(max(t))
print(min(t))


li = [1, 2, 3, 4, 5]
print(li)

t = tuple(li)
print(t)

s = "Hello"
print(s)
t = tuple(s)
print(t)


t = 1, "Ram", 8.5, 10, 20, 30, 40
print(t)
print(type(t))


# roll, name, marks, x = t
roll, name, marks, *other = t
print(roll)
print(name)
print(marks)
# print(x)
print(other)


"""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t)

# using index
for i in range(0, len(t)):
    print(i, "->", t[i])

# direct element access

for i in t:
    print(i)


i = 0
while i < len(t):
    print(t[i])
    i = i + 1
