a = 3
b = 7
c = a + b
for c in range(5):
    print("Current number is ", c)
    c += 1
print("Done")
a, b, i, t = 0, 1, 0, 0
print("Fibonacci sequence:")
for i in range(19):
    print(a)
    t = a
    a = b
    b = t+b
    i =+ 1
