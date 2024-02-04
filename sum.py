# step#1:start
# step#2:print "To add two numbers.\n"
# step#3:print "Enter the first number: "
# step#4:read num1
# step#5:print "Enter the second number: "
# step#6:read num2
# step#7:sum = num1 + num2
# step#8:print "Sum of " + num1 + " and " + num2 + 
#       " is " + sum + ".\n"
# step#9:stop

# print "To add two numbers.\n"
# print("To add two numbers.\n")

# print "Hai"
# print "Hello"

print("To add two numbers.")
print("Enter the first number: ", end="")
num1  = int(input())
print("Enter the second number: ", end="")
num2 = int(input())
sum = num1 + num2
print("Sum of ", num1, " and ", num2, " is ", sum, ".\n", sep="", end="")