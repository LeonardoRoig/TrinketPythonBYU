print ("Welcome to Grade Calculator")
print ("-")*50

math_score = int(raw_input("What is your Math Score: "))
print ("-")*50
english_score = int(raw_input("What is your English Score: "))
print ("-")*50
pe_score = int(raw_input("What is your PE Score: "))
print ("-")*50
science_score = int(raw_input("What is your Science Score: "))
print ("-")*50
art_score = int(raw_input("What is your Art Score: "))
print ("-")*50
print ("_")*50

def grade_number(subject, number_result):
  if 93 <= number_result <= 100:
      grade= "A"
  elif 90 <= number_result <= 93:
      grade = "A-"
  elif 87 <= number_result <= 90:
      grade = "B+"
  elif 83 <= number_result <= 87:
     grade = "B"
  elif 80 <= number_result <= 83:
      grade = "B-"
  elif 77 <= number_result <= 80:
      grade = "C+"
  elif 73 <= number_result <= 77:
     grade = "C"
  elif 70 <= number_result <= 73:
     grade = "C-"
  elif 67 <= number_result <= 70:
      grade = "D+"
  elif 63 <= number_result <= 67:
      grade = "D"
  elif 60 <= number_result <= 63:
      grade = "D-"
  elif 0 <= number_result <= 60:
      grade = "F"
  
  print " Your %s score is %d, you got a %s " % (subject, number_result, grade)
  print ("_")*50
  
grade_number("Math" , math_score)
grade_number("English", english_score)
grade_number("PE", pe_score)
grade_number("Science", science_score)
grade_number("Art", art_score)
