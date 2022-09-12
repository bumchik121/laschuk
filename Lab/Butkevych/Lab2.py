price = str(input("Enter the price of ur product "))

if not price:
   quit(None)
elif price.isalpha(): 
   quit(price)
elif int(price) <= 100 :
   discount = 0
   print("Ur didcount = " + str(discount))
elif int(price) > 100 and int(price) <= 500:
   discount = 0.03 * int(price)
   print("Ur discount = " + str(discount))
elif int(price) > 500 and int(price) <= 1000:
   discount = 0.05 * int(price)
   print("Ur discount = " + str(discount))   
elif int(price) > 1000:
   discount = 0.1 * int(price)
   print("Ur discount = " + str(discount))
