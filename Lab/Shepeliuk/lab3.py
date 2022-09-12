L = list(range(1,11))
for i  in range(len(L) - 4):
    if L[i]%2 == 0:
        del L[i]
print (L)

# A = [i for i in range (1,16)]
# print("L = ",A) 
# A = [i**2 for i in range (1,16)]
# print("L = ",A)

# list = [23,236,645,32,43,234,433,54,237,434,54,54] 
# print(max(list))