#3Write a program that asks the user for a number of seconds and prints out 
#how many minutes and seconds that is. For instance, 200 seconds is 3 
#minutes and 20 seconds.
# take input
x=int(input("enter seconds::"))
y=60
# RESULT by operations 
print ( str(x//y) + " minutes and " , str(x%y) +  " second" )

