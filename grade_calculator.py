def calculate_grade(marks):
  if marks >= 90:
    return "A"
  elif marks >= 80:
    return "B"
  elif marks >= 70:
    return "C"
  elif marks >= 60:
    return "D"
  else:
    return "F"

def get_message(grade):
  if grade == "A":
    return "Excellent work! keep it up!"
  elif grade == "B":
     return "Great Job! Keep improving."
  elif grade == "C":
     return "Good effort! You can do even better."
  elif grade == "D":
     return "Keep practicing! You can improve."
  else:
    return "Don't give up! Keep learning and try again. "

student_name = input("Enter student name: ")

while True:
    try:
         marks = int(input("Enter your marks (0-100): "))
         if 0<= marks<=100:
          break
         else:
          print("Invalid marks! Please enter a value between 0 and 100.")

    except ValueError:
          print ("Invalid input! Please enter only numerical values.")
grade = calculate_grade(marks)
message = get_message (grade)

print ("\n========STUDENT GRADE RESULT=======")
print ("Student Name:",student_name)
print ("Marks:",marks)
print ("Grade:",grade)
print ("Message:",message)
print ("===================================")