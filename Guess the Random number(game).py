#Guess the random number in given range.
import random


print("If you want to quit enter: quit")

guess=''
while True :
    print()
    score=0
    number=str(random.randint(1,10))
    if guess != 'quit':
        number_of_chances=1
        while number_of_chances<=3:
            guess=input("Input from user: " )
            
            if guess == 'quit' :
                break
            else:
                number_of_chances+=1
                if int(guess)<int(number):
                    print("have one more try!","Your guess was too small.")
                elif int(guess)>int(number):
                    print("have one more try!","Your guess was too high.")
                else:
                    score+=1
                    print("Congrat's! Your guess was correct.")
        if guess != 'quit':
            if score==0:
                print("Better Luck Next Time.")
            else:
                print("Your winning score:",score)
        else:
            break
    else :
        break
    else: 
        print("invalid")








