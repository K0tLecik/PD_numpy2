from numpy import *

print("Zadanie 1:")

a = arange(3)
b = arange(3,6,1)
print(a,b,a*b)

print("Zadanie 2:")

a = array([[7, 4, 2], [1, 1, 3], [0, 9, 6]])
b = array([[3, 1, 5, 1], [9, 8, 7, 5], [1, 3, 2, 4], [5, 7, 3, 0]])
print(a)
print(b)

print(a.min(axis=0), a.min(axis=1))
print(b.min(axis=0), b.min(axis=1))

print("Zadanie 3:")

a = arange(3)
b = arange(3,6,1)
print(dot(a,b))

print("Zadanie 4:")

a = arange(3)
b = linspace(3,4,3)
print(a*b)

print("Zadanie 5 - 7:")

a = sin(array([[2,3], [6,2], [1,1]]))
b = cos(array([[4,2], [1,7], [9,2]]))
print(a+b)

print("Zadanie 8:")

a = array([[7, 4, 2], [1, 1, 3], [0, 9, 6]])
for x in a:
    print(x)

print("Zadanie 9:")

a = array([[7, 4, 2], [1, 1, 3], [0, 9, 6]])
for x in a.flat:
    print(x)

print("Zadanie 10:")

a = arange(81).reshape((9,9))
print(a)
b = a.reshape((3,27))
print(b)

print("Zadanie 11:")

a = arange(12)
a = a.reshape((3,4))
print(a)
b = arange(12)
b = b.reshape((4,3))
print(b)
c = arange(12)
c = c.reshape((2,6))
print(c)
a = a.ravel()
b = b.ravel()
c = c.ravel()
print(a,b,c)