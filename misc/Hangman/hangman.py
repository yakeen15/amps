from turtle import *
import time
import csv
import random

print("Welcome to hangman!")
print("You know the rules and so do I!")
print("You will have to guess the names of the faculty members of the Department of Applied Mathematics of the University of Dhaka.")
print("Best of luck!")

#IMPORT CSV FILE
name_list = open('names list.csv', 'r')
names_obj = csv.reader(name_list)
names = list(names_obj)

#RANDOMLY SELECT A NAME FROM THE CSV FILE
name_read = names[random.randint(0, len(names))]
name = name_read[0]

#CONVERT THE NAME INTO A LIST TO OPERATE EASILY
name_list = list(name)
temp = []

#CREATE THE PUZZLE FORM OF THE NAME WITH UNDERSCORES
for i in range(len(name)):
    if 'A' <= name[i].upper() <= 'Z':
        temp.append('_')
    else:
        temp.append(name_list[i])

print(''.join(temp))

penup()
goto(-80,-100)
penup()
write("Welcome to hangman!")
goto(-110, -120)
write("You know the rules and so do I!")
goto(-175, -140)
write("You will have to guess the names of the faculty members of")
goto(-185, -160)
write("the Department of Applied Mathematics of the University of Dhaka.")
goto(-60, -180)
write("Best of luck!")
penup()
goto(30,-50)
pendown()

#CREATE THE STAGE FOR HANGING
forward(100)
back(200)
forward(100)
left(90)
forward(250)
left(90)
forward(80)
left(90)


#INITIALIZE THE SETTER FOR THE FIGURE TO AVOID REPETITION
set1 = False
set2 = False
set3 = False
set4 = False
set5 = False
set6 = False

#THE PLAYER WILL GET 5 LIVES
j = 1
while j < 7:
    guess = input("Guess a letter: ")
    set = False
    for i in range(len(name)):
        if name[i].upper() == guess.upper():
            temp[i] = name[i]
            set = True
    
    #COUNT OUT AN EXTRA LIFE IF GUESSED WRONG
    if set == True:
        pass
    else:
        j += 1

    print(''.join(temp))

    if ''.join(temp) == name:
        print("Congrats.")
        break
    
    #IF GUESSED A LETTER CORRECT, TRY GUESSING THE ENTIRE NAME
    if set == True:
        full_name = input("Guess the full name: ").upper()
        if full_name == name.upper():
            print("Congrats!")
            break
        else:
            print("Nice try!")
            
    #DRAWING THE HANGMAN
    #ROPE
    if j == 2:
        if set1 == False:
            forward(30)
            right(90)
            set1 = True
    #HEAD
    if j == 3:
        if set2 == False:
            circle(20)
            set2 = True
    #NECK
    if j == 4:
        if set3 == False:
            circle(20, 180)
            right(90)
            forward(20)
            set3 = True
    #ARMS
    if j == 5:
        if set4 == False:
            right(90)
            forward(50)
            back(100)
            forward(50)
            left(90)
            set4 = True
    #TORSO
    if j == 6:
        if set5 == False:
            forward(50)
            set5 = True
    #LEGS
    if j == 7:
        if set6 == False:
            left(45)
            forward(50)
            back(50)
            right(90)
            forward(50)
            penup()
            goto(-40, 160)
            pendown()
            forward(8)
            back(4)
            right(90)
            forward(4)
            back(8)
            right(180)
            penup()
            goto(-60, 160)
            pendown()
            forward(8)
            back(4)
            right(90)
            forward(4)
            back(8)
            set6 = True

        penup()
        goto(100,100)
        penup()
        write("Hanged!")
        
hideturtle()
time.sleep(5)
