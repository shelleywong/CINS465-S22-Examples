myInt = 42
print(myInt)
print("hello " + str(myInt))

myFloat = 3.1
print(myFloat)

myBool = True
print(myBool)

def myFunc():
    myString = "hello world"
    print(myString)

myFunc()

mylist = []
mylist2 = [1,2,3]
mylist3 = [1, "2", 3.0]

mylist3.append(True)
mylist3 += [False]

mylist3 = [4] + mylist3

print(mylist)
print(mylist2)
print(mylist3)
print(mylist3[1])
print(mylist3[2:4])

mylist3[0] = 0

print(mylist3)

i = 0
while i < len(mylist3):
    print(mylist3[i], end=" ")
    i += 1
print()

for j in range(len(mylist3)):
    print(mylist3[j])

for elem in mylist3:
    print(elem)

# mydict = dict() # object notation
mydict = {}
mydict['h'] = "hello"
print(mydict)

md = {
    "key1": "value1",
    "key2": "value2"
}
print(md)

mt = (1,2)
print(mt)

md[mt] = mylist3
print(md)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Bob", 38)
print(p)
print(p.name)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s: %d years old" % (self.name, self.age)

p = Person2("Mo", 40)
print(p)
print(p.name)
