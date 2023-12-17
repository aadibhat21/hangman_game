import random
import time
import os
import os.path
from urllib import request

#function to show current highscore
def showScore():
  bestName = ""
  #checks if file exists - if not then it creates one
  path = './scores.txt'
  checkFile = os.path.isfile(path)
  if checkFile == False:
    print("\nYou are the first person to play this game!\n")
    f = open('scores.txt', "x")
    f.close()
  else:
    #if file exists, then checks if there are any scores yet
    readFile = open('scores.txt', "r")
    firstLine = readFile.readline()
    readFile.close()
    if firstLine == "":
      print("\nYou are the first person to play this game!\n")
    else:
      #finds the highest score and prints it
      readFile = open('scores.txt', "r")
      bestScore = 0
      moreLines = True
      while moreLines:
        scoresRead = readFile.readline()
        if scoresRead == "":
          moreLines = False
        else:
          
          field = scoresRead.split(",")
          currentScore = int(field[1])
          if bestScore < currentScore:
            bestName = field[0]
            bestScore = currentScore
      readFile.close()
      print("\nThe highest score on your device is listed below:\n")
      print(bestName + ": " + str(bestScore) + " points")

def saveScore():
  bestName = ""
  nameSure = False
  if score > 0:
    print("You found the word in " + str(elapsed_time) + " seconds.")
    print("Also, you took", str(incorrect_attempts), "tries to find the word!\n")
    while nameSure == False:
      name = input("\nPlease enter your username: \n")
      correctInput = False
      #name checking + input checking
      while correctInput == False:
        confirm = input("\nAre you sure you want to use the username " + name + "? [y/n]\n")
        if confirm == "y" or confirm == "Y":
          nameSure = True
          correctInput = True
          print("\nThank you!")
        elif confirm == "n" or confirm == "N":
          print("\nPlease try entering your username again.")
          correctInput = True
        else:
          print("That is not a valid response. Try again.")
        #add score to file
    writeFile = open('scores.txt', "a")
    writeFile.write(name + "," + str(score) + "\n")
    writeFile.close()
    #show current highscore
    readFile = open('scores.txt', "r")
    print("\nThe highest score on your device is listed below:\n")
    bestScore = 0
    moreLines = True
    while moreLines:
      scoresRead = readFile.readline()
      if scoresRead == "":
        moreLines = False
      else:
        field = scoresRead.split(",")
        currentScore = int(field[1])
        if bestScore < currentScore:
          bestName = field[0]
          bestScore = currentScore
    readFile.close()
    print(bestName + ": " + str(bestScore) + " points")
  else:
    print("Get your b***h a*s out of here. You're actually so weird bro. 💀💀💀\n ")

# Generating random word for hangman subroutine
def randomWord():
  #checks if file exists - if not then it creates one
  path = './words.txt'
  wordFile = os.path.isfile(path)
  if wordFile == False:
    # Define the remote file to retrieve
    wordsURL = 'https://raw.githubusercontent.com/aadibhat21/final_word_list/main/words.txt '
    # Define the local filename to save data
    wordFile = 'words.txt'
    # Download remote and save locally
    request.urlretrieve(wordsURL, wordFile)
  with open('words.txt', 'r') as file:
    word_list = file.read().splitlines()
  return random.choice(word_list)

# Showing the dashes subroutine
def showDashes(chosenWord, entered_letters):
    for char in chosenWord:
        if char in entered_letters:
            print(char.upper(), end=" ")
        else:
            print("_", end=" ")
    print("\n")
           
# Initiating variables
chosenWord = randomWord()

# Getting user's letter subroutine with error checking
def getLetter():
    # Initiating variables
    global score
    global incorrect_attempts
    global playerWon
    playerWon = False
#    play_again = True
#    while play_again:
    chosenWord = randomWord()
    entered_letters = set()
    attempts = 0
    incorrect_attempts = 0
    max_attempts = 8
    wordFound = False

    start_time = time.perf_counter()
    while incorrect_attempts < max_attempts:
        global elapsed_time
        elapsed_time = time.perf_counter() - start_time
        elapsed_time = round(elapsed_time)
        print(f"\nElapsed Time: {elapsed_time} seconds\n")
        print(f"Attempts left: {max_attempts - incorrect_attempts}")
        print(f"\nGuess the {len(chosenWord)} letter word: \n")
        showDashes(chosenWord, entered_letters)
        print("Guessed Letters:", "".join(sorted(entered_letters)).upper())
            
        userLetter = input("Enter a letter: ").lower()

        if len(userLetter) == 1 and userLetter.isalpha():
            if userLetter not in entered_letters:
                entered_letters.add(userLetter)
                if userLetter not in chosenWord:
                    incorrect_attempts += 1
                    if wordFound == False:
                      print("_" * 55)
                      print("\nIncorrect guess.")
                    if incorrect_attempts == 1:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |               ")
                        print("    |               ")
                        print("    |               ")
                        print("    |               ")
                        print("    |               ")
                        print("    |__________     \n")
                         
                    elif incorrect_attempts == 2:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |               ")
                        print("    |               ")
                        print("    |               ")
                        print("    |               ")
                        print("    |__________     \n")
                    elif incorrect_attempts == 3:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |               ")
                        print("    |               ")
                        print("    |__________     \n")
                    elif incorrect_attempts == 4:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          /    ")
                        print("    |               ")
                        print("    |__________     \n")
                    elif incorrect_attempts == 5:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          / \  ")
                        print("    |               ")
                        print("    |__________     \n")
                    elif incorrect_attempts == 6:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |           |/  ")
                        print("    |           |   ")
                        print("    |          / \  ")
                        print("    |               ")
                        print("    |__________     \n")
                          
                    elif incorrect_attempts == 7:
                        print("     ____________   ")
                        print("    |           |   ")
                        print("    |           |   ")
                        print("    |          ( )  ")
                        print("    |          \|/  ")
                        print("    |           |   ")
                        print("    |          / \  ")
                        print("    |               ")
                        print("    |__________     \n")
                else:
                  if wordFound == False:
                    print("_" * 55)
                    print("\nThat is a correct guess!")
                        
            else:
                print("_" * 55)
                print("\nYou already entered this letter. Try again.")
        else:
            print("_" * 55)
            print("\nPlease enter a valid single letter.")

        if set(chosenWord).issubset(entered_letters):
            wordFound = True
            print("\nCongratulations! You guessed the word:", chosenWord.upper())
            end_time = time.perf_counter()
#            print(f"\nYou took {elapsed_time} seconds to guess the word")
            if elapsed_time < 15:
                score_multiplier = 10
            elif elapsed_time < 25:
                score_multiplier = 8
            elif elapsed_time < 40:
                score_multiplier = 5
            elif elapsed_time < 60:
                score_multiplier = 3
            elif elapsed_time > 120:
                score_multiplier = 0
            else:
                score_multiplier = 1
            score = (max_attempts - incorrect_attempts) * score_multiplier
            if score > 0:
              print("_" * 55)
              print("\nYour score is " + str(score) + " points. Well done!!!\n")
            else:
              print("\nWTH bro why are you so into this game? \nOmds you took over 2 mins on this. 💀💀💀")
            playerWon = True
            break

    if incorrect_attempts == max_attempts:
        print(f"\nGAME OVER. The word was: {chosenWord.upper()}")
        end_time = time.perf_counter()
        playerWon = False
            
        print("     ____________   ")
        print("    |           |   ")
        print("    |           |   ")
        print("    |          (X)  ")
        print("    |          \|/  ")
        print("    |           |   ")
        print("    |          / \  ")
        print("    |               ")
        print("    |__________     ")

#        while True:
#            play_again_input = input("\nDo you want to play again? (y/n): ").lower()
#            if play_again_input not in ['y', 'Y', 'N', 'n']:
 #               print("\nPlease enter y/n")
 #           elif play_again_input == "n" or play_again_input == "N":
  #              play_again = False
   #             break
    #        elif play_again_input == "y" or play_again_input == "Y":
     #           break
            

quitGame = False

while quitGame == False:
  #main menu
  
  print("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗")
  print("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║")
  print("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║")
  print("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║")
  print("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║")
  print("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝ \n")

  print("\nPlease choose what you would like to do:\n")
  print("1 - Play the game")
  print("2 - See previous high scores")
  print("3 - Learn the rules")
  print("4 - Quit Game\n")
  option = input("")
  #player wants to play
  if option == "1":
    print("_" * 55)
    getLetter()
    if playerWon == True:
      saveScore()
    else:
      print("\nTaking you back to the main menu...")
  #player wants to see previous highscore
  elif option == "2":
    print("_" * 55)
    showScore()
  #player wants to see the rules
  elif option == "3":
    print("_" * 55)
    print("\nrules go here")
  #player wants to quit game
  elif option == "4":
    print("_" * 55)
    print("\nThank you for playing. We hope you enjoyed our game!\nCreated by A. Bhat and H. Amane")
    quitGame = True
  #error check
  else:
    print("Please choose a valid option.\n")


