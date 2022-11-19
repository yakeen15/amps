import random

print("GUESSING GAME!")
print("Guess the number between 0 and 9. You have three attempts.")
print("After each guess, the terminal will tell you if your guess is bigger or smaller than the number.")
message = ["First attempt", "Second attempt", "Last attempt"]
num = random.randint(0, 9)
for x in range(3):
    try:
        print(message[x])
        guess = int(input("Guess: "))
        if -1 < guess < 10:
            if guess == num:
                print("Congratulation!")
                break
            elif guess > num:
                print("The number you guessed is bigger.")
            elif guess < num:
                print("The number you guessed is smaller.")
        else:
            print("You have to guess between 0 and 9.")
    except ValueError:
        print("You did not enter a vaild integer.")
