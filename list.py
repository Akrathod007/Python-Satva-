"""
Collection of Python :
1. List -> mutable and ordered
2. Tupel -> immutable and ordered
3. dictionary -> mutable and unordered
4. set -> mutable and unordered
"""

# List -> It is collection of multiple data types

# li = [1, 2, 3, 4, 5, 6, 7]
# #     0  1  2  3  4  5  6
# #  -  7  6  5  4  3  2  1
# print(li)
# print(type(li))
# # indexing
# print(li[0])
# print(li[5])
# # print(li[10]) #Error
# print(li[-1])
# print(li[-3])
# # print(li[-10]) #Error

# # slicing
# print(li[1:5])  # 1 to 4
# print(li[2:])
# print(li[:6])
# print(li[:])
# print(li[1:6:1])
# print(li[1:6:2])
# print(li[-2:-6])
# print(li[-6:-2])
# print(li[-2:-6:-1])
# print(li[-2:-7:-2])
# print(li[::-1])
# print(li[6:0:-1])
# print(li[2:-3])


# l1 = [1, 2, 3, 4, 5, 6]
# print(l1)

# l2 = [1, 3.14, "Hello", "Bye", True, None]
# print(l2)

# l3 = []
# print(l3)

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(li)
# print(len(li))

# index :
# for i in range(0, len(li)):
#     print(i, "->", li[i])

# direct element :
# for i in li:
#     print(i)


# i = 0

# while i < len(li):
#     print(i, "->", li[i])
#     i += 1

"""

li = [1, 2, 3, 4, 5, 6, 7, 8, 5, 9, 10]
print(li)

li.append(100)
print(li)
li.insert(4, 400)
print(li)
# removedElm = li.pop()
# removedElm = li.pop(7)
# removedElm = li.pop(17)

# print(removedElm)

# li.remove(5)
# li.remove(12)
# print([].pop()) #Error

# print(li)

print(li.index(5))
print(li.index(5, 6))
# print(li.index(5, 6, 8))
# print(li.index(15))

print("---------------------------------------------------------------")

li2 = [11, 12, 13, 14, 15]

# li.extend(li2)

# print(li)

li3 = li + li2
print(li3)

print(li2 * 3)

# li.clear()
# print(li)

print(li.count(5))
# li.reverse()
# li.sort()
li.sort(reverse=True)
print(li)

print(sum(li))
print(max(li))
print(min(li))

"""

# a = [1, 2, 3, 4]
# b = a
# c = a.copy()
# d = a[:]
# print(a)
# print(b)
# print(c)
# print(d)

# b[2] = 200
# c[1] = 1000
# d[3] = 3000
# print(a)
# print(b)
# print(c)
# print(d)

# count = int(input("Enter a number of element you want : "))
# li = []

# for i in range(1, count + 1):
#     n = int(input("Enter a element you want to add in list : "))
#     li.append(n)

# print(li)

# create even and odd list from given list of numbers :
# li = [23,45,66,88,76,45,34,21,56]

# create pos, neg and zero list from given list of numbers :
# li = [-34,67,89,-12,-4,0,0,-67,12]


"""
l1 = [1,2,3,4]
l2 = [3,4,5,6]

1. l3 = [1,2,3,4,3,4,5,6]

2. common = [3,4]

3. unique = [1,2,5,6]
"""

li = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]

print(li)
print(len(li))
print(li[2])
print(li[2][2])
print(li[2][0:2])
print(li[0:3][1:3])

for i in range(0, len(li)):
    print(i, "->", li[i])
    for j in range(0, len(li[i])):
        print(j, "->", li[i][j])

for i in li:
    for j in i:
        print(j)

"""
r and c

r = 2
c = 2

45 67 89 23

[
    [45,67],
    [89,23]
]
"""
