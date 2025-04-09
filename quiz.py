quiz = [
    {
        "Question": "1. How many bits are in a byte?",
        "options": ["A. 10", "B. 8", "C. 6", "D. 4"],
        "answer": "B"
    },
    {
        "Question": "2. A collection of items is referred to as:",
        "options": ["A. list", "B. Dictionary", "C. variable", "D. tuple"],
        "answer": "A"
    },
    {
        "Question": "3. Which of the following is NOT a primitive data type in mmost programming languages?",
        "options": ["A. Integer", "B. Float", "C. String", "D. Array"],
        "answer": "D"
    },
    {
        "Question": "4. What is the process of finding and fixing erors in a program called?",
        "options": ["A. Compiling", "B. Debugging", "C. Executing", "D. Linking"],
        "answer": "B"
    },
    {
        "Question": "5. Which of the following sorting algorithms has the best average-case time complexity?",
        "options": ["A. Bubble sort", "B. Insertion sort", "C. Merge sort", "D. Selection sort"],
        "answer": "C"
    }
]

correct = 0
wrong = 0
score = 0
for question in quiz:
    print(question["Question"])
    
    for option in question["options"]:
        print(option)

    answer = input("Select option: ")
    
    if answer.lower() == question["answer"].lower():
        print("Correct")
        correct +=1
        score += 5
    else:
        print(f"Incorrect, the correct answer is {question["answer"]}.")
        wrong += 1
        
print(f"Your total score is {score} and you have gotten {correct} correct and {wrong} wrong.")


