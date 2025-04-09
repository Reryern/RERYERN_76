scores = []

def add_scores(value):
    if value > 0:
        scores.append(value)
    else:
        print("Value must be above 0")

    return value

def list_scores(scores):
    for value in scores:
        print(value)

    return scores

#Ask the user to enter a score
while True:
    number = input("Enter a value or a to quit: ")
    if number.lower() == "a":
        break
    
    add_scores(int(number))

list_scores(scores)


def compute_sum(scores):
    total = 0
    for value in scores:
        
        total += value
    print(f"Your total is {total}.")

    return total

compute_sum(scores)

def get_max(scores):
    max = 0
    for value in scores:
        if value > max:
            max = value
    print(f"The max value is {max}")

    return max

get_max(scores)





    