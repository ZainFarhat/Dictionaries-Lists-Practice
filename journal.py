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
