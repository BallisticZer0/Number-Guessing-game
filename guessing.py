import random

Number = random.randint(1,100)

def The_Number_guessing_game():
    Gueses = 8
    print("This is a number guessing game")
    while(Gueses > 0):	# While loops make it so that you just do everything
			# While this condition holds
			# So while you have more guesses than 0
        print("You have",Gueses,"atempts left")
        guess = int(input('Take a guess from 1 to 100:   '))

        # So here we are checking if guess is low
        if guess < Number:
            print("The number is Higher...")
            Gueses -= 1
        # If guess is high
        elif guess > Number:
            print("The number is Lower...")
            Gueses -=1
        # The case that we have guessed the right number
        else:
            print()
            print("Congrates you got it right :) The number was", Number)
            print("You guessed it with", Gueses , " atempts left")
        
        #    break
        # So here I would recommend starting the use of returns
            return(1)
        # Now note that you really don't have to but it can be helpful 
        

    # Have left the wihle loop - means we have no more guesses
    # Check if last guess was correct?
    if guess != Number:
        print()
        print('Sorry you reached the maximum number of tries')
        print('The number was', Number)


# I'm not sure what you are meaning with this,
# But I think you are meaning what happens when we don't enter a number or 
# we only enter a charecter?

# So that we can handle in the 'The_Number_guessing_game:
# Have a check - if(quess.isdigit())
# what that will do is it will check to make sure the input string is only a digit - i.e - "1","2",etc

#def No_press_buttons(characters):
#    npb = ""
#    characters = "qwertyuiopasdfghjklzxcvbnmQWRETYUIOPASDFGHJKLZXCVBNM!@#$%^&*\|]}[{':;',.<>?"
#    for npb in range(npb):
#        print("Thats not a number.")




# So this would be the Main part of the code:
#while input("Shall we play a game? [y|n] ") == 'y':
# So we already had either a while or for loop in the function call so all we need to do is:
start = input("Shall we play a game? [y|n] ")
# If we start and get a yes start game
if(start.lower()=='y' or start.lower() =='yes'):
    The_Number_guessing_game()
# If we start but get a no don't start game
elif start.lower()=="n" or start.lower() == "no":
    print("Ok, GoodBye\n")
# Otherwise we have some odd input and need the user to clarify:
else:
    print("Can you please type y for YES and n for NO")
    #if input(characters):
    #    print("Can you please type y for YES and n for NO")
    #
    #elif input('Shall we play a game? [y|n]') == 'n':
    #    print("Ok, GoodBye")

