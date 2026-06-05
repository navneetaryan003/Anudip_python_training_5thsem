player_score=[]  #taking a empty list

#input of score from user
for i in range(4):
    score=int(input("enter the score{}".format(i+1)))   #.format is to write the value in {}
    player_score.append(score)

print("player score ")

print("store of 11 players",player_score)

#initialiosation of max_score assuming first number is the maximum for comparison
max_score=player_score[0]

for i in range(1,len(player_score)):
   
   if(player_score[i]>max_score):    #comparison with the next elements 
       max_score=player_score[i]     #updating the value if condition is true


print(max_score)    #printing the maximum 