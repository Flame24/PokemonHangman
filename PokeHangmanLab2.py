#Josue Bohorquez
#Revised Pokemon Hangman Game
#Lab 6

import random

#Ask the user for their name and provides a greeting
def askName():
    userName = str(input('What is your name?')) 
    print ('Hello'+ str(userName) +' Welcome to Pokemon Hangman!')
#Asks the user if they want to play the GAME or not
def intro():
    count = 0
    while count < 1:
        userAns = str(input('Do you want to play Pokemon hangman? Yes or No? '))
        if (userAns =='Yes') or (userAns =='No'):
            if (userAns =='Yes'):
                return 'Yes'
                count += 1
            else:
                print('aww man.')
                return 'No'
                count += 1
        else:
            print('Invalid input. Yes or No ')
#This function explains the rules and randomly picks a POKEMON name from the list in Dictorinary
def rules(): 
    print('''\nHere is how it goes.
            \n1.The game will ask you which generation pokemon you want to choose from and it will randomly choose one from the dictionary
            \n2.You have a total of six attempts before the pokemon word gets revealed.\n''')
    count = 0
    while count < 1:
        userAns = str(input('Which Generation Pokemons do you want?\n1 , 2 , 3 , or 4. '))
        if (userAns =='1'):
            print ('Here is the list of the Pokemons.')
            for poke in pokemon_Dict()[userAns]:#prints out all the names in the name list
                print ('-'+poke)
            return pick_Rand(userAns).upper()#randomly picks a name and returns the name in all uppercase letters
            count = 1#ends while loop
        elif (userAns =='2'):
            print ('Here is the list of the Pokemons.')
            for poke in pokemon_Dict()[userAns]:#prints out all the names in the name list
                print ('-'+poke)
            return pick_Rand(userAns).upper()#randomly picks a name and returns the name in all uppercase letters
            count = 1
        elif (userAns =='3'):
            print ('Here is the list of the Pokemons.')
            for poke in pokemon_Dict()[userAns]:#prints out all the names in the name list
                print ('-'+poke)
            return pick_Rand(userAns).upper()#randomly picks a name and returns the name in all uppercase letters
            count = 1
        elif (userAns =='4'):
            print ('Here is the list of the Pokemons.')
            for poke in pokemon_Dict()[userAns]:#prints out all the names in the name list
                print ('-'+poke)
            return pick_Rand(userAns).upper()#randomly picks a name and returns the name in all uppercase letters
            count = 1
        else:
            print('Incrorrect, please choose from 1 , 2 , 3 , or 4.\n')

def pokemon_Dict():#dictionary of list of names of 1-4 gen pokemons
    poke_Dict ={
        "1":
        [
            'Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie',
            'Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate',
            'Spearow','Fearow','Ekans','Raichu','Sandshrew','Sandslash','Nidoran','Nidorina','Nidoqueen','Slowbro'
        ],
        "2":
        [
            "Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret",
            "Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn",
            "Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos"            
        ],
        "3":
        [
            "Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena",
            "Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre",
            "Ludicolo","Seedot","Nuzleaf","Shiftry","Nincada","Ninjask","Shedinja","Taillow","Swellow","Shroomish"            
        ],
        "4":
        [
            "Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly",
            "Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew",
            "Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam","Mothim","Combee","Vespiquen"            
        ]
    }
    return poke_Dict

def pick_Rand(gen_pick):#picks a random name from the list of names
    rand = random.randint(0,29)
    pokeList = pokemon_Dict()[gen_pick]
    return (pokeList[rand])

def pickRand():#picks a random name from the lists
    rand = random.randint(0,29)
    pokeList = pokemonBank()
    return (pokeList[rand])

def pokemonBank():#list of pokemon names returns all capitalized letters
    pokeName = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie',
                'Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate',
                'Spearow','Fearow','Ekans','Raichu','Sandshrew','Sandslash','Nidoran','Nidorina','Nidoqueen','Clefairy',]
    for name in range(len(pokeName)):
        pokeName[name] = pokeName[name].upper()
    return (pokeName)

def trackLetter(name):#takes randomly picked name and returns '_' for each letter
    spaceName = []
    for i in range(len(name)):
        spaceName.append('_')
    return spaceName

def makeList(secretWord):#takes secret word(randomly picked name) and turns it into a list
    secretList = []
    for letter in secretWord:
        secretList.append(letter)
    return secretList
   
def userGuess():#checks if user input is valid
    count = 0
    while count < 1:
        userAns = str(input('Guess a letter. '))
        if (userAns.isalpha() == True) and (len(userAns) == 1):
            userAns = userAns.upper()
            return userAns
            count += 1
        else:
            print('Invalid input. Guess a letter ')

def wrongLetters(wrong): #keeps track of wrong letters
    wrongList.append(wrong)
    return wrongList
    
def correctLetters(guess):#check if user guessed a letter in the secret word. updates list from trackLetter function
    for i in range(len(rightList)):
        if rightList[i] == guess:
            emptyList[i] = guess
    return

def sameLetter(guess):#tells user message if same letter is guessed more than once
    for i in range(len(rightList)):
        if (trackEmptyList[i] == guess):
            print('You have guessed that letter already. Guess another letter.')
            return False
    for i in range(len(wrongList)):
        if (wrongList[i] == guess):
            print('You have guessed that letter already. Guess another letter.')
            return False

def rightWrong(guess):#checks if guessed letter is in randonly picked name
    if (sameLetter(guess) == False):
        correctLetters(guess)
        return False
    else:
        correctLetters(guess)#update the emptyList. shows correct letters
        if (trackEmptyList != emptyList):
            print(HANGMAN_PICS[guessCount])
            print("That letter is in the pokemon's name.")
            return True
        elif (trackEmptyList == emptyList):#if the updated emptyList has not been updated because user didnt guess a letter in the name
            print("\n\nThat letter is NOT in the pokemon's name.\nHere is the list of incorrect guess(es).")
            print(wrongLetters(guess))
            return

def playAgain():#asks if user wants to play POKEMON HangMan again 
    count = 0
    while count < 1:
        userAns = str(input('Do you want to play again? Yes or No? '))
        if (userAns =='Yes') or (userAns =='No'):
            if (userAns =='Yes'):
                return 'Yes'
            else:
                return 'No'
            count += 1
        else:
            print('Invalid input. Yes or No ')

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

wrongList = []#makes empty list. used in wrongLetters function
askName()
count = 0
if (intro() == 'No'):#if user input is no, while loop does not run. End of program. 
    count = 1
while (count < 1):
    secretWord = rules()#Sets secretWord to a randomly picked name from a list that the user picked
    print(HANGMAN_PICS[0])
    
    emptyList = trackLetter(secretWord)#appends '_' to emptyList for every letter in name
    rightList = makeList(secretWord)#randomly pick name from(type)str to (type)list
    copyList = emptyList[:]#makes another list with the same element as emptyList
    guessCount = 0
    while (guessCount < 6):
        print(emptyList)#prints the empty spaces for letters in the randomly picked name
        if rightList == emptyList:
            print('You got it, you rock!')
            wrongList.clear()#resets wrongList for next game
            if (playAgain() == 'Yes'):
                emptyList = copyList[:]#resets emptyList for next game
                guessCount = 6
                continue
            else:
                guessCount = 6#breaks inside while loop
                count +=1#breaks outside while loop. end of program
                print('Have a nice day')
                break
        guess = userGuess()#stores valid user guess
        trackEmptyList = emptyList[:]#makes another list with the same element as emptyList
        guessCheck = rightWrong(guess)#checks if user input is right or wrong
        if (guessCheck == True):
            continue
        elif (guessCheck == False):
            continue
        print(HANGMAN_PICS[guessCount+1])#if guess is wrong, add body part to hangman
        guessCount += 1
        if (guessCount == 6):#user ran out of tries
            print("You ran out of guesses :( \nThe pokemon's name was "+secretWord)
            wrongList.clear()#resets wrongList for next game
            if (playAgain() == 'Yes'):
                emptyList = copyList[:]
                guessCount = 6
            else:
                print('Have a nice day!')
                count += 1#Causes end of program
