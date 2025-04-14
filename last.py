students = []

while True:
    student_name = input("Enter student name or q to exit: ")
    if student_name.lower() == "q":
        print("Thank you for your time.")
        break
    student_course = input("Enter the student course: ").lower()
    reg_number = input("Enter the reg number of student: ")
    age = int(input("Enter the age of the student: "))
    gender = input("Enter the gender of the student: ")

    scores = []

    for i in range(4):
        student_score = int(input("Enter the student score: "))
        scores.append(student_score)

    details = {
        "Name": student_name,
        "Course": student_course,
        "Registration number": reg_number,
        "Age": age,
        "Gender": gender,
        "Scores": scores,
    }
    
    students.append(details)

def display_student():
    for student in students:
        print(f"The name of the student is {student.get("Name")} \n The course is {student.get("Course")} \n The gender is {student.get("Gender")}")


def student_list_by_course(course):
    for student in students:
        if details.get("Course") == course:
            print(student.get("Name"))

student_list_by_course("bit")

    


