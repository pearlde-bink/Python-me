def prime(n):
    if n<2: return False
    else:
        for i in range(2, n):
            if n % i == 0: 
                return False
                break
    return True

n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if prime(a[i]): b.append(a[i])
for i in range(len(b)):
    print(b[i], end=" ")
"""
a=[int(input()) for i in range(n)]

def Prime(n):
    if n<2: return False
    else:
        for i in range(2,n):
            if n%i==0: return False
    return True
result=[i for i in a if Prime(i)]
print(*result, end=" ")
"""