def subtractGame():
    import math, random

    print(
"""
WELCOME TO THE SUBTRACTION GAME!!!

Instructions: 

This is a turn-based game against the machine.

You will start by making three critical strategy choices:
(i) A starting number to subtract from;
(ii) Whether you or the machine will go first
(iii) Whether the machine will play optimally or naively

To win the game, your goal is to reduce the original number to zero in your last turn. 

""")
    
    gameOn = 1

    while gameOn:
        
        while True:
            try:
                startNum = int(input('\nWhat will the starting number be? '))
                if startNum < 3:
                    raise Exception()
            except Exception as e:
                print("\nPlease input a valid integer greater than 3")
            else:
                break
        
        currVal = startNum

        while True:
            try:
                aiMode = int(input("\nShould the machine play naively (0) or optimally (1) "))
                if aiMode not in [0,1]:
                    raise Exception()
            except Exception:
                print("\nPlease input either a zero (0) or a one (1) to make your selection.")
            else:
                break
        
        while True:
            try:
                myTurn = int(input('\nWould you like to make the first move (input 1), or let the machine go first (input 0)? '))
                if myTurn not in [0,1]:
                    raise Exception()
            except Exception:
                print("\nPlease input either a zero (0) or a one (1) to make your selection.")
            else:
                break
        

        while currVal > 0:
            if myTurn:
                while True:
                    try: 
                        subtractBy = int(input("\nSubtract one (1) or two (2)? "))
                        if subtractBy not in [1,2]:
                            raise Exception()
                    except Exception:
                        print("You can only subtract by one (1) or (2). Try again.")
                    else:
                        break
                currVal -= subtractBy
                print(f'\nThe new value is {currVal}.')
                myTurn = 0
            else:
                if aiMode and (currVal % 3 != 0):
                    subtractBy = currVal % 3
                else:
                    subtractBy = math.ceil(random.random() * 2)
                
                currVal -= subtractBy
                print(f'\nThe other player has subtracted by {subtractBy}. \n\nThe new value is {currVal}.')
                myTurn = 1
        
        if not myTurn:
            print('\nYOU WIN!!!')
        else:
            print('\nYOU LOSE...')

        while True:
            try:
                gameOn = int(input("\nWould you like to play again? Yes (input 1) or no (input 0): "))
                if gameOn not in [0,1]:
                    raise Exception()
            except Exception:
                print("\nPlease input either a zero (0) or a one (1) to make your selection.")
            else:
                break

    return None


subtractGame()