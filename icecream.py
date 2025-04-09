# A program to customize the ice cream order and automatically calculate the cost of their ice cream.

container = input("What container would you like to use?(cup or cone): ")

cup = 50
cone = 80
if container == "cup" or "cone":
    scoops = int(input("How many scoops would you like?: "))

    if scoops <= 4:
        cost_of_scoops = scoops * 1
        flakes = input("Would you like flakes?(yes or no): ")
        chocolate_sprinkle = input("Would you like chocolate sprinkle?(yes or no): ")
        strawberry = input("Would you like strawberry?(yes or no): ")
        if flakes == "yes":
           cost_of_flakes = 40
           cost = cost_of_scoops + cost_of_flakes + cup or cone
        else:
            cost = cost_of_scoops + cup or cone

        if chocolate_sprinkle == "yes":
            cost_of_chocolate_sprinkle = 30
            cost = cost + cost_of_chocolate_sprinkle + cup or  cone
        else:
            cost = cost_of_scoops + cup or cone

        if strawberry == "yes":
            cost_of_strawberry = 60
            cost = cost + cost_of_strawberry + cup or  cone
        else:
            cost = cost_of_scoops + cup or cone
    else:   
        print("Sorry, we only have 4 scoops available")
'''if container == "cone":
    scoops = int(input("How many scoops would you like?: "))
    if scoops <= 4:
        cost_of_scoops = scoops * 1
        flakes = input("Would you like flakes?(yes or no): ")
        chocolate_sprinkle = input("Would you like chocolate sprinkle?(yes or no): ")
        strawberry = input("Would you like strawberry?(yes or no): ")
        if flakes == "yes":
           cost_of_flakes = 40
           cost = cost_of_scoops + cost_of_flakes + cone
        else:
            cost = cost_of_scoops + cone
        
        if chocolate_sprinkle == "yes":
            cost_of_chocolate_sprinkle = 30
            cost = cost + cost_of_chocolate_sprinkle + cone
        else:
            cost = cost_of_scoops + cone

        if strawberry == "yes":
            cost_of_strawberry = 60
            cost = cost + cost_of_strawberry + cone
        else:
            cost = cost_of_scoops + cone
    else:
        print("Sorry, we only have 4 scoops available")'''
print(f"Your total cost is {cost} Ugx")
