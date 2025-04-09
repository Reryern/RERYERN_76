#Write a program to capture student name and the coursework mark and exam score out of 100. Coursework mark is captured out of 40, exam score out of 100.Program should compute the final coursework mark out of 30 and the exam mark out of 70 and the final mark. The program should also determine the student grade basing on the final score.

student_name = input("What is the student name: ")

coursework_mark = int(input("What is the coursework mark: "))

exam_score = int(input("What is the exam score: "))

course_work = (coursework_mark/40)*30

exam_mark = (exam_score/100)*70

final_exam_mark = course_work + exam_mark

print(course_work)

print(exam_mark)

print(final_exam_mark)

if final_exam_mark >= 80:
    print("A")
elif final_exam_mark >= 70:
    print("B")
elif final_exam_mark >= 60:
    print("C")
elif final_exam_mark >= 50:
    print("D")
else:
    print("F")