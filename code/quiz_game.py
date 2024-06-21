
#printing logo for quiz and Welcome msg
print("\______   \____ |  | __ ____   _____   ____   ____  ")
print(" |     ___/  _ \|  |/ // __ \ /     \ /  _ \ /    \ ")
print(" |    |  (  <_> )    <\  ___/|  Y Y  (  <_> )   |  \ ")
print(" |____|   \____/|__|_ \\___  >__|_|  /\____/|___|  / ")
print("                     \/    \/      \/            \/ ")
print("\t \t"+"Welcome to Pokemon Quiz")

#score system variable to keep a track for the score
score=0

#asking the user if they want to play or not 
answer=input("Do you want to play Pokemon Quiz?\n")

#if user doesnot want to play , this msg will be displayed
if answer.lower()!="yes" :
     print("I see you are not in the mood.Have a nice day!")
     quit()

#if user wants to play

#Ist question
q1=input("Q1.Who is the main character in Pokemon series\n")

if q1.lower()=="ash ketchum":
     print("Correct!The correct answer is Ash Ketchum\n")
     score+=1
     print("You got 1 point for that,your current score is "+str(score)+"\n")

else:
     print("Wrong! The correct answer is Ash Ketchum\n")
     print("You got 0 point for that,your current score is "+str(score)+"\n")


#2nd Qustion
q2=input("Q2.Which type is super effective against Water-type Pokémon?\n")

if q2.lower()=="electric and grass":
     print("Correct!The correct answer is ELectric and Grass\n")
     score+=1
     print("You got 1 point for that,your current score is "+str(score)+"\n")

else:
     print("Wrong! The correct answer is Electric and Grass\n")
     print("You got 0 point for that,your current score is "+str(score)+"\n") 

#3rd Question
q3=input("Q3.Which Pokémon is known as the 'Genetic Pokémon'?\n")

if q3.lower()=="mewtwo":
     print("Correct!The correct answer is Mewtwo\n")
     score+=1
     print("You got 1 point for that,your current score is "+str(score)+"\n")

else:
     print("Wrong! The correct answer is Mewtwo\n")
     print("You got 0 point for that,your current score is "+str(score)+"\n") 


#4th Question

q4=input("Q4.What is the maximum number of Pokémon a trainer can carry at one time?\n")

if q4.lower()=="six":
     print("Correct!The correct answer is six\n")
     score+=1
     print("You got 1 point for that,your current score is "+str(score)+"\n")

else:
     print("Wrong! The correct answer is six\n")
     print("You got 0 point for that,your current score is "+str(score)+"\n") 

#5th Question
q5=input("Q5.In what year was the first Pokémon game released?\n")

if q5.lower()=="1996":
     print("Correct!The correct answer is 1996\n")
     score+=1
     print("You got 1 point for that,your current score is "+str(score)+"\n")

else:
     print("Wrong! The correct answer is 1996\n")
     print("You got 0 point for that,your current score is "+str(score)+"\n") 

print("You have completed the quiz!\n")
print("You have answered "+str(score)+" out of 5 correctly!!")
print("Your score is "+str((score/5)*100)+"%")

print("Thanks for playing!")


print("⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀                 ")
print("⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄           ")
print("⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀       ")
print("⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦      ")
print("⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ")
print("⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉     ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣶")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⠿")
print("⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀       ")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      ")
print("⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟      ")
print("⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀       ")
print("⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀       ")
print("⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀      ")
