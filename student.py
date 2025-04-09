#A program to ask the user to enter student names and enter the score in english, math, science and art. Get the total score of all the subjects, compute the average score

Name = input("Enter name of the student: ")

#display  only the first name of the student in uppercase
Name.index(" ")
print(Name[:7])

English_score = int(input("English scores: "))
Math_score = int(input("Math score: "))
Science_score = int(input("Science score: "))
Art_score = int(input("Art_score: "))

total_score = English_score + Math_score + Science_score + Art_score

print(total_score)

average_score = total_score / 4

print(average_score)

percentage_score = (total_score/ 400) *100 
print(percentage_score)