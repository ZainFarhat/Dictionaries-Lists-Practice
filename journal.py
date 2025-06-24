#Part 1: Rebuilding the Journal

# jumbled list called records. It contains student names and their grades
records = [
  ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
  ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
  ["Jana", 94], ["Ziad", 75]
]

# Creating an empty dictionary called class_journal
class_journal = {}

# loop through each item in the list having a name and a grade
for record in records:
  name = record[0]
  grade = record[1]

  # Check if the student's name is already in the dictionary
  if name in class_journal:
    class_journal[name].append(grade)  # add the grade to their existing student's name list.
  else:
    class_journal[name] = [grade]  # create a new student name list  with their grade

# Display the results of Each student's name their list of grades
for student in class_journal:
  print(student, ":", class_journal[student])


#Part 2: The Basic Report

  # pass by  each student name we saved in the class_journal dictionary,
for student in class_journal:
  grades = class_journal[student]  # grab the grades list
  total = 0  # total sum of all grades

  # pass by each grade and add to the total
  for grade in grades:
    total = total + grade

  #Calculate their average grade (rounded to 2 decimal places)
  average = total / len(grades)  
  average = round(average, 2)  

  # print name, grades, and average , a dotted line to seperate between students average .
  print("-------------") 
  print("Student Name :", student)
  print("Grades:", grades)
  print("Average of " + student + ": " + str(average))
  print("-------------") 

#Part 3: Deeper Analysis

highest_avg = 0 # This will starts with 0 untill we find the highest average.
highest_avg_student = "" # An empty string to save the name of the student with the highest average .


smallest_range = 100  # Starting value.
most_consistent_student = ""

students_with_low_grade = []

total_grades = 0
sum_of_all_grades = 0

# pass by each student
for name in class_journal:
  grades = class_journal[name]  # grab their grades
  total = 0

  for grade in grades:
    total += grade

  average = total / len(grades) 

  if average > highest_avg:
    highest_avg = average
    highest_avg_student = name  # Student having the highest Average

# Most consistent performance 
  grade_range = max(grades) - min(grades)  
  if grade_range < smallest_range:
    smallest_range = grade_range
    most_consistent_student = name

  # list of students with any grade below 70
  for grade in grades:
    if grade < 70: 
      if name not in students_with_low_grade:
        students_with_low_grade.append(name)
  
  total_grades += len(grades)
  sum_of_all_grades += total  

# Overall Class Average
class_average = round(sum_of_all_grades / total_grades, 2)

# Display the results results
print("Student with the highest average is:", highest_avg_student, "with", round(highest_avg, 2))
print("Most consistent performance :", most_consistent_student, "with range of", smallest_range)
print("Students with a grade < 70:", students_with_low_grade)
print("Total number of grades:", total_grades)
print("Overall class average is:", class_average)

# Save to file
file = open("class_analysis_report.txt", "w")
file.write("Student with the highest average is: " + highest_avg_student + " having " + str(round(highest_avg, 2)) + "\n")
file.write("Most consistent performance :" + most_consistent_student + " with range of " + str(smallest_range) + "\n")
file.write("Students with a grade < 70:" + ", ".join(students_with_low_grade) + "\n")
file.write("Total number of grades: " + str(total_grades) + "\n")
file.write("Overall class average is " + str(class_average) + "\n")
file.close()
print("Check text file  'Class_Report.txt'")


# Existing class journal
class_journal = {
  "Layla": [89, 91, 86],
  "Tariq": [77, 84, 73],
  "Jana": [100, 97, 94],
  "Ziad": [62, 71, 75]
}

# New sets of grades
new_grades = [["Jana", 99], ["Ziad", 78], ["Layla", 84]]

# A new set of grades are added to the class_joirnal
for set in new_grades:
  name = set[0]
  grade = set[1]

  if name in class_journal:
    class_journal[name].append(grade)  # add the grade to their existing student's name list.
  else:
    class_journal[name] = [grade]      # create a new student name list  with their grade


highest_avg = 0
highest_avg_student = ""

smallest_range = 100 # Starting value.
most_consistent_student = ""

students_with_low_grade = []

total_grades = 0
sum_of_all_grades = 0



for name in class_journal:
  grades = class_journal[name]
  total = 0

  for grade in grades:
    total += grade

  average = total / len(grades)

  if average > highest_avg:
    highest_avg = average
    highest_avg_student = name

  grade_range = max(grades) - min(grades)

  if grade_range < smallest_range:
    smallest_range = grade_range
    most_consistent_student = name

  



