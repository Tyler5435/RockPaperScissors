import random

# Simple Rock-Paper-Scissors game implementation
# TODO: Consider refactoring to a Game class and avoid module-level globals

possibleChoices = ["rock", "paper", "scissors"]  # available moves

# Counters for tracking results across rounds
draws = 0
computerWins = 0
playerWins = 0


def main():
    # Entry point: show rules, run the game, then display results
    gameRules()
    playGame()
    gameResults()


def gameRules():
    # Print the game rules and pause until the user is ready
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
    # Play three rounds against the computer
    for i in range(3):
        computerChoice = random.choice(possibleChoices)  # computer picks at random

        print()
        print('Round ' + str(i + 1) + ':')
        print('--------')

        isValid = False

        # Repeat until the player provides a valid numeric choice
        while not isValid:
            try:
                userInput = int(
                    input('Enter 1 for Rock, 2 for Paper or 3 for Scissors: ')
                )

                if 1 <= userInput <= 3:
                    isValid = True
                else:
                    # Input number out of range
                    print('Invalid input. Please enter a number between 1 and 3.')

            except ValueError:
                # Non-integer input
                print('ERROR: Invalid input. Please enter a number between 1 and 3.')

        # Map numeric input (1-3) to the choice string
        playerChoice = possibleChoices[userInput - 1]

        print()
        print('Computer chose: ' + computerChoice)
        print('You chose: ' + playerChoice)
        print()

        # Determine round result and display it
        result = rockPaperScissors(playerChoice, computerChoice)
        print(result)


def rockPaperScissors(playerChoice, computerChoice):
    # Resolve a single round and update global counters
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
    # Print final game statistics and the overall winner
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
        # Game-level draw
        print('The game ended in a draw!')

        input('\nPress Enter to exit the game...')


main()
