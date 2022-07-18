def age_finder(a):
    b = a.split('/')
    age = 2022 - int(b[2])
    return age
a =str(input('enter Dob'))
b = age_finder(a)
print(b)
