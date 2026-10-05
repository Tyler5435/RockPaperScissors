import random

possibleChoices = ["rock", "paper", "scissors"]

draws = 0
computerWins = 0
playerWins = 0

def main():
    gameRules()
    playGame()
    gameResults()

def gameRules():
    print('Rock, Paper, Scissors Rules')
    print('--------------------------------------------------')
    print('1. Each game consists of three rounds.')
    print('2. Select 1 for Rock, 2 for Paper or 3 for Scissors.')
    print('3. Each round follows these rules:')
    print('   * Rock blunts Scissors.')
    print('   * Paper wraps Rock.')
    print('   * Scissors cuts Paper.')
    print('4. The player with the most wins wins the game.')
    print('--------------------------------------------------')
    print()

    # Pause until the player presses Enter.
    input('Press Enter to start the game...')

def playGame():
    for i in range(3):
        computerChoice = random.choice(possibleChoices)

        print()
        print('Round ' + str(i + 1) + ':')
        print('--------')

        isValid = False

        while not isValid:
            try:
                userInput = int(
                    input('Enter 1 for Rock, 2 for Paper or 3 for Scissors: ')
                )

                if 1 <= userInput <= 3:
                    isValid = True
                else:
                    print('Invalid input. Please enter a number between 1 and 3.')

            except ValueError:
                print('ERROR: Invalid input. Please enter a number between 1 and 3.')

        playerChoice = possibleChoices[userInput - 1]

        print()
        print('Computer chose: ' + computerChoice)
        print('You chose: ' + playerChoice)
        print()

        result = rockPaperScissors(playerChoice, computerChoice)
        print(result)

def rockPaperScissors(playerChoice, computerChoice):
    global draws, computerWins, playerWins

    if computerChoice == playerChoice:
        draws += 1
        return "It's a draw!"

    elif computerChoice == "rock":
        if playerChoice == "paper":
            playerWins += 1
            return "You win! Paper wraps Rock."
        else:
            computerWins += 1
            return "Computer wins! Rock blunts Scissors."

    elif computerChoice == "paper":
        if playerChoice == "scissors":
            playerWins += 1
            return "You win! Scissors cuts Paper."
        else:
            computerWins += 1
            return "Computer wins! Paper wraps Rock."

    elif computerChoice == "scissors":
        if playerChoice == "rock":
            playerWins += 1
            return "You win! Rock blunts Scissors."
        else:
            computerWins += 1
            return "Computer wins! Scissors cuts Paper."

def gameResults():
    print()
    print('Game Results')
    print('------------')
    print('Draws: ' + str(draws))
    print('Computer Wins: ' + str(computerWins))
    print('Player Wins: ' + str(playerWins))
    print('------------')

    if playerWins > computerWins:
        print('Congratulations! You won the game!')
    elif computerWins > playerWins:
        print('Computer won the game! Better luck next time.')
    else:
        print('The game ended in a draw!')

        input('\nPress Enter to exit the game...')

main()