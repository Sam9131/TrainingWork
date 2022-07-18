class add:
    def add(a,b):
        sum = a + b
        return(sum)
    def subtract(a,b):
        sub = a - b
        return(sub)
    def multiply(a,b):
        mul= a*b
        return(mul)
a = int(input('enter vallue a'))
b = int(input('enter value b'))

print(add.add(a, b))

class p2:
    def fun3():
        print("I am inside")
class child(add, p2):
    def fun2():
        print('i am inside')



b = child.multiply(a, b)
print(b)