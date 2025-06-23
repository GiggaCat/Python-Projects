import random
computer = random.randint(1,100)
i = -1
guesses = 1
while (i != computer):
    user = int(input("Guess the number: "))
    if (user > computer):
        print("Lower number please!!!")
        guesses +=1
    elif (user < computer):
        print("Higher number please!!!")
        guesses +=1
    else:
       print(f"You guessed the right number {computer} in {guesses} attempt")
       break