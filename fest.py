games = ["Network", "Coding", "Repair", "Quiz"]
groups = ["CYBER", "SYNTAX", "CODERS"]

group_scores = []


for group in groups:
    print(f"\t{group}")
    games_scores = []
    

    for game in games:
        score = int(input(f"Enter the score for {game}: "))
        games_scores.append(score)
    
    group_scores.append(games_scores)
    
for group_score in group_scores:
    total_score = 0
    for score in group_score:
        total_score += score
    print(total_score)

print("\n\tGROUP\t\tnetwork\tcoding\trepair\tquiz\ttotal")
index = 0
for group in group_scores:
    output=f'\t{groups[index]}\t'
    total = 0

    for score in group:
        output+=f"\t{score}"
        total +=score
    index +=1
    print(f"{output}\t{total}")