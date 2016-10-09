def win_rate(arr, wins, total, k):
    team_1, team_2 = None, None
    prev = 0
    
    for i in xrange(len(arr)):
        if i%7 == 2:
            team_1 = ' '.join(sorted(arr[prev:i+1]))
            prev = i+1
        elif i%7 == 5:
            team_2 = ' '.join(sorted(arr[prev:i+1]))
        elif i%7 == 6:
            if arr[i] == 'true':
                wins[team_1] = wins[team_1]+1 if team_1 in wins else 1
            else:
                wins[team_2] = wins[team_2]+1 if team_2 in wins else 1
            
            total[team_1] = total[team_1]+1 if team_1 in total else 1
            total[team_2] = total[team_2]+1 if team_2 in total else 1
            prev = i+1

    pairs = []
    for team in total:
        if team not in wins:
            pairs.append((team, 0))
        else:
            pairs.append((team, float(wins[team])/total[team]))    # FLOAT DIVISION
    return sorted(pairs, key=lambda x: x[1])[::-1][:k]

def main():
    wins = {}
    total = {}
    arr = [
        "Yuna","Bianca","Camille","Zelda","Monica","Ashley","true",
        "Ashley","Samus","Zelda","Bianca","Elissa","Rain","false",
        "Hailey","Gina","Camille","Ivy","Jynx","Bianca","true",
        "Xena","Bianca","Jynx","Tanya","Xena","Daisy","false",
        "Xena","Valorie","Daisy","Xena","Bianca","Peach","true",
        "Xena","Peach","Elissa","Lara","Unity","Elissa","false",
        "Hailey","Monica","Felise","Jynx","Hailey","Gina","true",
        "Gina","Queen","Jynx","Felise","Wendy","Hailey","false",
        "Kelly","Unity","Felise","Queen","Gina","Olivia","true",
        "Unity","Monica","Hailey","Jynx","Gina","Lara","false",
        "Gina","Valorie","Natalie","Hailey","Queen","Tanya","true",
        "Ivy","Yuna","Samus","Queen","Ivy","Jynx","false",
        "Valorie","Yuna","Lara","Kelly","Monica","Natalie","true",
        "Unity","Xena","Natalie","Tanya","Monica","Rain","false",
        "Queen","Natalie","Peach","Peach","Samus","Zelda","true",
        "Tanya","Zelda","Yuna","Olivia","Valorie","Xena","false",
        "Elissa","Rain","Bianca","Bianca","Yuna","Camille","true",
        "Daisy","Xena","Valorie","Camille","Hailey","Gina","false",
        "Xena","Tanya","Daisy","Felise","Hailey","Monica","true",
        "Hailey","Wendy","Felise","Unity","Lara","Elissa","false",
        "Kelly","Unity","Felise","Natalie","Valorie","Gina","true",
        "Yuna","Valorie","Lara","Gina","Lara","Jynx","false",
        "Jynx","Ivy","Queen","Natalie","Queen","Peach","true",
        "Xena","Valorie","Olivia","Tanya","Monica","Rain","false",
        "Hailey","Gina","Camille","Rain","Bianca","Elissa","true",
        "Elissa","Unity","Lara","Daisy","Xena","Tanya","false",
        "Gina","Lara","Jynx","Unity","Kelly","Felise","true",
        "Queen","Ivy","Jynx","Tanya","Monica","Rain","false",
        "Lara","Gina","Jynx","Hailey","Gina","Camille","true",
        "Xena","Daisy","Tanya","Tanya","Monica","Rain","false",
        "Tanya","Monica","Rain","Jynx","Gina","Lara","true"
    ]
    k = 3
    result = win_rate(arr, wins, total, k)
    for i, j in result:
        print i, j

if __name__ == '__main__':
    main()
    
# 
# Your previous Plain Text content is preserved below:
# 
# In the game of Super Smash Gals, 6 players choose a character from a selection screen to compete in
# 3 vs 3 fighting mayhem. Nintenda, a Japanese game company, wants to calculate which three character
# teams have the highest win rate in their game.
#   
# The input is below:
#     [
#         "Yuna","Bianca","Camille","Zelda","Monica","Ashley","true",
#         "Ashley","Samus","Zelda","Bianca","Elissa","Rain","false",
#         "Hailey","Gina","Camille","Ivy","Jynx","Bianca","true",
#         "Xena","Bianca","Jynx","Tanya","Xena","Daisy","false",
#         "Xena","Valorie","Daisy","Xena","Bianca","Peach","true",
#         "Xena","Peach","Elissa","Lara","Unity","Elissa","false",
#         "Hailey","Monica","Felise","Jynx","Hailey","Gina","true",
#         "Gina","Queen","Jynx","Felise","Wendy","Hailey","false",
#         "Kelly","Unity","Felise","Queen","Gina","Olivia","true",
#         "Unity","Monica","Hailey","Jynx","Gina","Lara","false",
#         "Gina","Valorie","Natalie","Hailey","Queen","Tanya","true",
#         "Ivy","Yuna","Samus","Queen","Ivy","Jynx","false",
#         "Valorie","Yuna","Lara","Kelly","Monica","Natalie","true",
#         "Unity","Xena","Natalie","Tanya","Monica","Rain","false",
#         "Queen","Natalie","Peach","Peach","Samus","Zelda","true",
#         "Tanya","Zelda","Yuna","Olivia","Valorie","Xena","false",
#         "Elissa","Rain","Bianca","Bianca","Yuna","Camille","true",
#         "Daisy","Xena","Valorie","Camille","Hailey","Gina","false",
#         "Xena","Tanya","Daisy","Felise","Hailey","Monica","true",
#         "Hailey","Wendy","Felise","Unity","Lara","Elissa","false",
#         "Kelly","Unity","Felise","Natalie","Valorie","Gina","true",
#         "Yuna","Valorie","Lara","Gina","Lara","Jynx","false",
#         "Jynx","Ivy","Queen","Natalie","Queen","Peach","true",
#         "Xena","Valorie","Olivia","Tanya","Monica","Rain","false",
#         "Hailey","Gina","Camille","Rain","Bianca","Elissa","true",
#         "Elissa","Unity","Lara","Daisy","Xena","Tanya","false",
#         "Gina","Lara","Jynx","Unity","Kelly","Felise","true",
#         "Queen","Ivy","Jynx","Tanya","Monica","Rain","false",
#         "Lara","Gina","Jynx","Hailey","Gina","Camille","true",
#         "Xena","Daisy","Tanya","Tanya","Monica","Rain","false",
#         "Tanya","Monica","Rain","Jynx","Gina","Lara","true"
#     ]
#   
#   
# Every 7 elements in the array represents a match result. For example, for the first match:
#     - "Yuna", "Bianca", "Camille" represents the LEFT team.
#     - "Zelda", "Monica", "Ashley" represents the RIGHT team.
#     - "true" means LEFT team won and RIGHT team lost.
#   
# Given an input with any number of matches, find the team with the highest win rate.
#     - Note: 1 win & 0 losses = 100% win rate. 0 wins and 1 loss = 0% win rate. 1 win and 1 loss = 50% win rate.

