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

class child(add):
    def fun2():
        print('i am inside')



b = child.multiply(a, b)
print(b)