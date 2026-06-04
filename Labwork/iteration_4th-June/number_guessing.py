secret_number=int(input("enter the secret number"))
attempt=0
while (True):
    guess_number=int(input("enter the number you guess"))
    attempt+=1
    if(secret_number==guess_number):
        print("correct guess")
        break
    if(guess_number<secret_number):
        print("too low")
    else:
        print("too high")
    