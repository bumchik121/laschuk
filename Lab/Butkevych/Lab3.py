import random


#_________task_1___________________________________________
li = []
l_size = int(input("enter the list size "))

for i in range(0, l_size):
   li.append(int(random.randrange(1, 100)))
print("filled out list: ", li)


#_doesn't work_______________
# for z in li:
#    if z % 2 == 0:
#       li.remove(z)
# print(li)
#____________________________


dli = []
for el in li:
   if el %2 == 0:
      dli.append(el)   
fli = []

#1st compare lists method for loop
for x in li:
   if x not in dli:
      fli.append(x)
print("even numbers removed: ", fli)   

#2nd compare lists method by set
# print("even numbers removed ", list(set(li) - set(dli)))


#_________task_2___________________________________________
for y in range(0, len(fli)):
   fli[y] **= 2
print("list items exponentiation by two: ", fli)



#_________task_3___________________________________________
#1 method finding the max number in list for loop  
maxi = fli[0]
for d in fli:
   if maxi < d:
      maxi = d
print("max number in the list: ", maxi)
  
  
  
#2 method finding the max number in list by max function   
# print("max number in the list: ", max(fli))