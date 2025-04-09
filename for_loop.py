students = ["Peter", "Joy", "Umar", "Musa"]
subjects = ["Math", "English", "Science", "SST"]

number_of_subjects = int(input("Enter number of subjects: "))
total = 0

for student in students:
    print(f"\n\tEnter {student}'s scores.")
    student_total = 0 

    for subject in subjects:
        subject_score = int(input(f"\t{subject} score: "))
        student_total += subject_score
        student_average = student_total/ number_of_subjects
    total += student_total 
        
    average = total/ number_of_subjects

    print(f"\tThe total for {student} is {student_total} and your average is {student_average}")

print(f"\n\tYour total is {total} and your average is {average}")
