a = (1,2,3,4,5)
print(a[0])
b = a.index(2)
print(b)
print(type(a[0]))
c = {1,2,34,1,6,7,7,8} 
print(c)
d = {'id' :1 ,'name': 'mady','roll no' :25}
print(d["id"])
print(d.keys())
print(d.values())
m = [{'id': 2},{'namer':'techie'},{'class':'csa'}]
print(m)
num = int(input())
if num == 0:
print("The number is zero")
elif num > 0:
    print("The number is a positive number")
else:
    print("The number is a negative number")
