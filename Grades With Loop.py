print ("Welcome to Grade Calculator!")
print ("-")*50
print ("Enter a number from 0 to 100")
count = 0
total = 0 
while count <5:
  grade = input("What was your score? ")
  value = int(grade)
  count = count + 1
  total= total + value
  average = total/count
if 93 <= average <= 100:
    print ("For an average score of " + str(average) + ", your grade is A")
elif 90 <= average <= 93:
    print ("For an average score of " + str(average) + ", your grade is A-")
elif 87 <= average <= 90:
    print ("For an average score of " + str(average) + ", your grade is B+")
elif 83 <= average <= 87:
    print ("For an average score of " + str(average) + ", your grade is B")
elif 80 <= average <= 83:
    print ("For an average score of " + str(average) + ", your grade is B-")
elif 77 <= average <= 80:
    print ("For an average score of " + str(average) + ", your grade is C+")
elif 73 <= average <= 77:
    print ("For an average score of " + str(average) + ", your grade is C")
elif 70 <= average <= 73:
    print ("For an average score of " + str(average) + ", your grade is C-")
elif 67 <= average <= 70:
    print ("For an average score of " + str(average) + ", your grade is D+")
elif 63 <= average <= 67:
    print ("For an average score of " + str(average) + ", your grade is D")
elif 60 <= average <= 63:
    print ("For an average score of " + str(average) + ", your grade is D-")
elif 0 <= average <= 60:
    print ("For an average score of " + str(average) + ", your grade is F ")
else:
    print ("ERRO")