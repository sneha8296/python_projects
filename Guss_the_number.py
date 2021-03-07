import random


Your_number =str(input("Enter your number "))
str(print("your number is"+Your_number))

num= str(random.randint(1,10))

str(print("number is "+num))

if Your_number==num:
               print("Congratulatios you are win,number is same ")
else:
               print("Sorry your are fail")