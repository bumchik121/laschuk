A=[]

i=0
while i<10:
    x=float(input("x= "))
    A=A+[x]
    i=i+1


print(A)

del A[len(A)-4]

print(A)

