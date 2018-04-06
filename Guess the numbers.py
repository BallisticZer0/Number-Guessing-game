import random

Number = random.randint(1, 100)




def The_Number_guessing_game():
    Gueses = 8
    print("This is a number guessing game")
    for gueses in range(Gueses):
        print("You have",Gueses,"atempts left")
        guess = int(input('Take a guess from 1 to 100:   '))


        if guess < Number:
            print("The number is Higher...")
            Gueses -= 1
        elif guess > Number:
            print("The number is Lower...")
            Gueses -=1

        else:
            print()
            print("Congrates you got it right :) The number was", Number)
            print("You guessed it with", Gueses ,"atempts left")
        

            break

    if guess != Number:
        print()
        print('Sorry you reached the maximum number of tries')
        print('The number was', Number)


def No_press_buttons(charchters):
    npb = ""
    charchters = "qwertyuiopasdfghjklzxcvbnmQWRETYUIOPASDFGHJKLZXCVBNM!@#$%^&*\|]}[{':;',.<>?"
    for npb in range(npb):
        print("Thats not a number.")
    if input(charchters):
        print("Can you please type y for YES and n for NO")
    

        


while input("Shall we play a game? [y|n] ") == 'y':
    The_Number_guessing_game()
    
if input == 'n': 
    print("Ok, GoodBye")
   





    

# add gesses, so when you guess it takes off a guess so you can see what your score was.





    


# need to add a play again choice.


# if any key is pressed:  # != is the not-equal-to operator
#    do_nothing()











# import livewire


# class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'


# print("This is a game where you need to Guess the number the computor is thinking of.\nIf you get this right congrats\nBUT, if you get it worng, sucks for you.")
