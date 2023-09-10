#python program to find the factorial of a number provided by the user.
#change the value for a different result
num=7
# to take input from the user
#num = int (input("enter a number:"))
factorial = 1
# check if the number is nagative,positive or zero
if num < 0:
  print("sorry, factorial does not exist for nagative numbers")
elif num == 0:
  print("the factorial of 0 is 1")
else:
  for i in range(1,num + 1):
    factorial = factorial*i
    print("the factorial of",num,"is",factorial)