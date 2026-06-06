# Write a program to:
# • Count half-centuries and centuries.
# • Find the highest score.
# • Display all scores below 20.
# • Calculate the average score.

#details of the score
scores = [45, 78, 12, 100, 67, 8, 90, 55]

count_centuries=0    #for counting centuries
count_half=0         #for counting half-centuries
sum=0                #iniliasation of sum for calculting sum of the score

#task1 : Count half-centuries and centuries.
for score in scores:

    if score==100:
        count_centuries+=1

    elif score>=50:
        count_half+=1


print("total number of centuries :",count_centuries)

print("total number of half-centuries :",count_half)

#task 2 : Find the highest score.

print("Highest score :",max(scores))

for score in scores:

    #task 3: Display all scores below 20.

    if score<20:
        print("scores below 20 :",score)
    
    sum+=score

       
#task 4 :Calculate the average score.

print("Average Score :",sum/len(scores))   
