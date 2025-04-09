students = []
marks = []
number_of_students = int(input("Enter the number of students: "))
number_of_subjects = 2

for name in range(number_of_students):
    name = input("Enter the name of the student: ")
    students.append(name)
    subject_score = []
    
    for subject in range(number_of_subjects):
        subject = input("Enter the subject: ")
        score = int(input(f"Enter the marks for {subject}: "))
        subject_score.append(score)
    
    marks.append(subject_score)


for mark in marks:
    total_mark = 0
    average = 0
    for score  in subject_score:
        total_mark += score
        average = total_mark/number_of_students 
    print(average)
    print(total_mark)

