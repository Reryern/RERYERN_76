scores = []
number_of_scores = 4

for number in range(number_of_scores):

    score = int(input("Enter the marks: "))

    scores.append(score)

even_sum = 0
odd_sum = 0
for number in range(number_of_scores):
    if score % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
    
print(f"The odd sum is {odd_sum}")
print(f"the even sum is {even_sum}")
        

print(scores)
