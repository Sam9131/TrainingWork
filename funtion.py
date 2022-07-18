def evenodd(n):
    if n%2 == 0:
        return "div by 2"
    else:
        return "not div by 2"

n = int(input())
a = evenodd(n)
print(a)