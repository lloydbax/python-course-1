students = []


def get_students_titlecase():
  students_titlecase = []
  for student in students:
    students_titlecase.append(student["name"].title())
  return students_titlecase

def print_student_titlecase():
  student_titlecase = get_students_titlecase()
  print(student_titlecase)

def add_student(name, student_id=0):
  student = {"name": name, "student_id": student_id}
  students.append(student)

def save_file(student):
  try:
    f = open("students.txt", "a")
    f.write(student + "\n")
    f.close()
  except Exception:
    print("Could not save file")

def read_file():
  try:
    f = open("students.txt", "r")
    for student in f.readlines():
      add_student(student)
    f.close()
  except Exception:
    print("Could not read file")

read_file()
print_student_titlecase()
create_student = input("Would you like to add a student? (y/n):")
while True:
  if create_student == 'y':
    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    add_student(student_name,student_id)
    save_file(student_name)
    create_student = input("Add another? (y/n): ")
    continue
  if create_student == 'n':
    break
  else:
    print("Read the instructions,")
    create_student = input("Try again! (y/n):")
    continue