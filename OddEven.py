#Assignment 2
#EVEN - When NUMBER is Divisible by 2 (Remainder is 0_)
#ODD - When NUMBER is NOT Divisible by 2 (Remainder is NOT 0_)
#% modulus operator

# print (9 % 2) (Remainder 1) #ODD
# print (8 % 2) (Remainder 0) #EVEN

num = int(input("Enter an integer :"))
if num % 2 == 0:
  print(f"{num} is an EVEN number.")
else:
  print(f"{num} is an ODD number.")