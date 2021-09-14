grade = int(input("What was your score? ")) 

if 93 <= grade <= 100:
  print  ("For a score of " + str(grade) + ", your grade is A")
elif 90 <= grade < 93:
  print  ("For a score of " + str(grade) + ", your grade is A-")
elif 87 <= grade < 90:
  print  ("For a score of " + str(grade) + ", your grade is B+")
elif 83 <= grade < 87:
  print ("For a score of " + str(grade) + ", your grade is B")
elif 80 <= grade < 83:
  print ("For a score of " + str(grade) + ", your grade is B-")
elif 77 <= grade < 80:
  print ("For a score of " + str(grade) + ", your grade is C+")
elif 73 <= grade < 77:
  print ("For a score of " + str(grade) + ", your grade is C")
elif 70 <= grade < 73:
  print ("For a score of " + str(grade) + ", your grade is C-")
elif 67 <= grade < 70:
  print ("For a score of " + str(grade) + ", your grade is D+")
elif 63 <= grade < 67:
  print ("For a score of " + str(grade) + ", your grade is D")
elif 60 <= grade < 63:
  print ("For a score of " + str(grade) + ", your grade is D-")
elif grade < 60:
  print ("For a score of " + str(grade) + ", your grade is F")