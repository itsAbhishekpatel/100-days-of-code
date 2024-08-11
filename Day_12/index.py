# guess the random number and win
import random 

random_num = random.randint(1,100)

def game():
    print("Welcome to the Random Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    choose = input("Choose a difficultty. Type 'easy' or 'hard': ")

    def guess(attemp):
        while attemp > 0:
            guess_num = int(input("make a guess: "))
            if guess_num == random_num:
                print("win")
                break
            elif guess_num < random_num:
                print("num is very low")
            elif guess_num > random_num:
                print("num is very high")
            attemp -= 1
                
            print(f"{attemp} attempt left") 
            if attemp == 0:
                print("You Loose")


    if choose == 'easy':
        attemp_10 = 10
        guess(attemp_10)

    elif choose == 'hard':
        attemp_5 = 5
        guess(attemp_5)
    
game()
# when you are writng code first write sudo code, divide the code into comments 


