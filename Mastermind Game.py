import random,time

def colouRight(sequence,playerGuess):
    tempseq = []
    tempseq += sequence
    for i in range(0,4):
        global col_right
        if playerGuess[i].upper() == tempseq[0]:
            col_right += 1
            tempseq[0] = ''
        if playerGuess[i].upper() == tempseq[1]:
            col_right += 1
            tempseq[1] = ''
        if playerGuess[i].upper() == tempseq[2]:
            col_right += 1
            tempseq[2] = ''
        if playerGuess[i].upper() == tempseq[3]:
            col_right += 1
            tempseq[3] = ''


#Variables:
col_right = 0
pos_right = 0
T_or_F = False
tries = 1
colours = ['R' , 'Y' , 'B' , 'G' , 'O' , 'W']
sequence = []
a = 0


print("""
___  ___          _                      _           _
|  \/  |         | |                    (_)         | |
| .  . | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |
| |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
| |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
\_|  |_/\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|

          """)
    

#Instructions:
print('''
This is a game of Mastermind, a famouse puzzle game. The rules are simple:                                             
- The computer will generate a sequence of four colours                                                                
- The colours consist of Red, Yellow, Blue, Green, Orange and White                                                    
- You, the player, has to guess the right order of the colours chosen by the computer                                  
- You only have 10 attemps to guess correctly though                                                                   
- Just type the first letter of the colour you think is in the sequence, remember to leave a space between each colour 
- But most of all, have fun!                                                                                           
''')

#Getting the sequence:
for i in range(1,5):
    seq = random.randint(0,5)
    sequence.append(colours[seq])


#Ask how many attempts the person wants to have:
while int(a) == 0:
    a = input('How many attempts would you like to try and guess the sequence:  ')
    if a == str:
        a = 0
    if a == int:
        a = int(a)
   
    
            


#Game loop:
while tries <= int(a):

    print('Attempt',tries,'of',a)
    print('\nGuess the sequence')
    playerGuess = []
    guess = input()
    playerGuess = guess.split()


    #Test to see if the sequence is the right length:
    while len(playerGuess) != 4:
        print('The sequence contains 4 colours.')
        guess = input()
        playerGuess = guess.split()
            

    #Test to see if player inputted the right colour:
    for i in range(0,6):
        if playerGuess[0].upper() == colours[i]:            
            for i in range(0,6):
                if playerGuess[1].upper() == colours[i]: 
                    for i in range(0,6):
                        if playerGuess[2].upper() == colours[i]:
                            for i in range(0,6):
                                if playerGuess[3].upper() == colours[i]:
                                    T_or_F = True
                                    a = 1


    #Test to see if the player, you, got any colours or possitions right:
    while T_or_F:

        col_right = 0
        pos_right = 0
        tries += 1


        #Test for the right colour in the right place:
        if playerGuess[0].upper() == sequence[0]:
            pos_right += 1
        if playerGuess[1].upper() == sequence[1]:
            pos_right += 1
        if playerGuess[2].upper() == sequence[2]:
            pos_right += 1
        if playerGuess[3].upper() == sequence[3]:
            pos_right += 1


        #Run the mini-function:
        colouRight(sequence,playerGuess)
        T_or_F = False


        #print how good or bad you did:
        print('You got,',col_right,'colours right and',pos_right,'in the right place.')
        time.sleep(1)
        
    if pos_right == 4:
        print('Well done! you beat the MasterMind.')
        break
        











        
