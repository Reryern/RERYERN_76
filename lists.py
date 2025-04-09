subjects = ["ENG", "MTC", "SCI", "SST"]

students = []

student_scores = []

no_of_students = int(input("No. of students: "))

for number in range(no_of_students):
    student = input("Student name: ")

    students.append(student)

    subject_scores = []

    '''for subject in subjects:
        score = int(input(f"\t{subject}: "))

        subject_scores.append(score)

    student_scores.append(subject_scores)

print(students)
print(student_scores)


print("\n\tSTUDENT \tENG \tMTC \tSCI \tSST\tTOTAL\tAVERAGE")
index=0
for student in student_scores:
    output=f'\t{students[index]}\t'
    no_of_subjects=4
    total=0
    average=0

    for score in student:    
        output+=f"\t{score}"
        total +=score
        average=total/no_of_subjects
    index +=1
    print(f"{output}\t{total}\t{average}")'''

