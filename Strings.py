a = 'hello'
b = 'bye'
c = [a, b]
print("The strings are {} and {}".format(a, b))
print(c)
print("*******************")

temp = a
a = b
b = temp

print("The strings are {} and {}".format(a, b))
print(c)
print("*******************")
def swap(x, y):
    temp = x
    x = y
    y = temp

swap(a, b)

print("The strings are {} and {}".format(a, b))
print(c)
print("*******************")


