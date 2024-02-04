# print("Hai")   # print "Hai\n"
# print("Hello") # print "Hello\n"

# print("Hai", end="")   # print "Hai"
# print("Hello", end="") # print "Hello"

# print("Hai", end="\n")
# print("Hai")

# print "To find sum of two numbers.\n"
# print "Enter the first number: "

# print("To find sum of two numbers.\n", end="")
# print("Enter the first number: ", end="")

# num1 = 5
# sq = num1 * num1
# print("The square of ", num1, " is ", sq, ".", sep="-")

# The square of  5  is  25 .

# num1 = 5
# num2 = 6
# sum = num1 + num2
# print(num1, num2, sum, sep="")

# print("To find sum of two numbers.\n", end="")
# print("Enter the first number: ", end="")
# num1 = int(input())
# print("Enter the second number: ", end="")
# num2 = int(input())
# sum = num1 + num2
# print("Sum of ", num1, " and ", num2, " is ", sum, ".\n", sep="", end="")


# print("Friends.\n", end="")
# print("Your good name: ", end="")
# name = input()
# print("Enter your friend's name: ", end="")
# friend = input()
# print(name, " and ", friend, " are friends.\n", sep="", end="")

# step#1: start
# step#2: print "Pass or fail.\n"
# step#3: print "Enter your marks: "
# step#4: read marks
# step#5: if (marks >= 80)
#           print "You have passed the exam.\n"
#           goto step#7
# step#6: print "You have failed the exam.\n"
# step#7: stop

# print("Pass or fail.\n", end="")
# print("Enter your marks: ", end="")
# marks = int(input())
# if (marks >= 80):
#     print("You have passed the exam.")
#     print("Go out and celebrate.")
# else:
#     print("You have failed the exam.")
#     print("Better luck next time.")


# step#1: start
# step#2: print "How many natural numbers you want? "
# step#3: read count
# step#4: counter = 1
# step#5: print "The natural numbers upto " + count + " are "
# step#6: if (counter < count)
#           print counter + ", "
#           counter = counter + 1
#           goto step#6
# step#7: print counter + ".\n"
# step#8: stop

# print("How many natural numbers you want? ", end="")
# count = int(input())
# counter = 1
# print("The natural numbers upto ", count, " are ", sep="", end="")
# while (counter < count):
#     print(counter, ", ", sep="", end="")
#     counter = counter + 1
# print(counter, ".\n", sep="", end="")


print("Enter your name: ", end="")
name = input()
print("The name is ", name, ".\n", sep="", end="")
# print("The first 3 characters are ")
# print(name[0])
# print(name[1])
# print(name[2])

print("How many character you want to show? ", end="")
count = int(input())
counter = 0
print("The first ", count, " characters are ", sep="", end="")
while (counter < count-1):
    print(name[counter], ", ", sep="", end="")
    counter = counter + 1
print(name[counter], ".\n", sep="", end="")