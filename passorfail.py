# step#1: start
# step#2: print "To check pass or fail.\n"
# step#3: print "Enter your marks: "
# step#4: read marks
# step#5: if (marks >= 80)
# 			print "You have passed in the exam.\n"
# 			goto step#7
# step#6: print "You have failed in 
# 		the exam.\n"
# step#7: stop

print("To check pass or fail.")
print("Enter your marks: ", end="")
marks = int(input())
if (marks >= 80):
    print("You have passed in the exam.")
if (marks < 80):
    print("You have failed in the exam.")


# prime < testcase-1.txt > testcase-1.out