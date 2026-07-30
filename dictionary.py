"""
student = {"name": "Ram", "age": 24, "city": "Ahm", "pin code": 2100}

print(student)
print(type(student))

person = dict(name="Suresh", age=28, city="Surat")
print(person)
print(type(person))

print(person["name"])
print(person.get("city"))
print(student["pin code"])
print(student.get("pin code"))
# print(person["pin code"])
print(person.get("pin code"))

"""

# del student["pin code"]
# print(student)


# val = student.pop("city")
# print(val)
# print(student)
"""
elm = student.popitem()
print(elm)
print(student)

student.clear()
print(student)


scoreBoard = {"Virat": 98, "Dhoni": 78, "Rohit": 88, "Gill": 92, "Suryakumar": 79}
print(scoreBoard)

for i in scoreBoard:
    print(i, "->", scoreBoard.get(i))
print("-------------------------------------------------")
for i in scoreBoard.keys():
    print(i, "->", scoreBoard.get(i))

print("-------------------------------------------------")

for i in scoreBoard.values():
    print(i)

for k, v in scoreBoard.items():
    print(k, "->", v)

scoreBoard["Dhoni"] = 95
print(scoreBoard)

scoreBoard["Sachin"] = 99
print(scoreBoard)


student = {"name": "Raju", "age": 21}
print(student.get("name"))
print(student.get("city", "Not Found"))

student = {"name": "Raju", "age": 21}
print(student.keys())
print(student.values())
print(student.items())


student = {"name": "Raju", "age": 21}
student.update({"age": 22, "city": "Surat"})
print(student)


student = {"name": "Raju", "age": 21}
new_student = student.copy()
print(new_student)

keys = ["math", "science", "english"]
marks = dict.fromkeys(keys, 0)
print(marks)

student = {"name": "Raju"}
print(student.setdefault("age", 20))
print(student.setdefault("name"))
print(student)

print(len(scoreBoard))

"""
"""
scoreBoard = {
    "Virat": [98, 67, 84],
    "Dhoni": [56, 89, 94],
    "Rohit": [77, 82, 79],
    "Sachin": [70, 85, 95],
    "Gill": [72, 82, 45],
}

print(scoreBoard)
print(scoreBoard["Rohit"])
print(scoreBoard.get("Rohit"))
print(scoreBoard.get("Rohit")[2])

x = scoreBoard.get("Rohit")
print(x[2])

scoreBoard["Sachin"][1] = 92
print(scoreBoard)


finalTotal = 0
for i in scoreBoard.keys():
    total = 0
    print(i, "->", scoreBoard[i])
    for j in scoreBoard[i]:
        total = total + j
    print("Total :", total)
    finalTotal = finalTotal + total

print("Final Total :", finalTotal)


"""

person = {"Name": "Raj", "Age": 21}
print(person)

rank = {1: "Raj", 2: "Ram", 3: "Manan"}
print(rank)

x = {(1, 2): "Hello", (3, 4): "Bye"}
print(x)

# y = {[1, 2]: "Hello"}
# print(y)

marks = {
    "Ram": {"Maths": 98, "Science": 87, "Arts": 91},
    "Shyam": {"Maths": 78, "Science": 97, "Arts": 81},
    "Raj": {"Maths": 88, "Science": 77, "Arts": 71},
}

print(marks)
print(marks.get("Shyam").get("Science"))


"""
1. Count Frequency of Words
sentence = "python is easy python is powerful"

data = {
    "python":2,
    "is":2,
    "easy":1,
    "powerful":1
}

2. Create Dictionary of Number and Cube
N = 10
data = {
    1:1,
    2:8,
    3:27
}

3. Swap Keys and Values
data = {"a": 1,"b": 2, "c": 3}
new_data = {1:"a",2:"b",3:"c"}

4. Create Dictionary From String Length
words = ["python", "java", "ai"]

data = {
    "python":6,
    "Java":4,
    "ai":2
}

5. Count Vowels in Sentence
sentence = "python programming"
data = {
    "a":
}

6. Create Dictionary of Factorials
N = 10
data = {
    1:1,
    2:2,
    3:6,
    4:24
}

7. Group Numbers by Positive and Negative
numbers = [10, -5, 7, -2, 0]

data = {
    "positive": [],
    "negative": [],
    "zero": []
}

8. Separate Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]

data = {
    "even": [],
    "odd": []
}
"""
