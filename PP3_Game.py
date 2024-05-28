# function to determine the outcome of the game
def outcome(user1, user2):
    if user1 == user2:
        return 'It\'s a tie!'
    elif user1 == 'rock':
        if user2 == 'paper':
            return user2 + ' beats ' + user1
        else:
            return user1 + ' beats ' + user2
    elif user1 == 'paper':
        if user2 == 'rock':
            return user1 + ' beats ' + user2
        else:
            return user2 + ' beats ' + user1
    elif user1 == 'scissors':
        if user2 == 'rock':
            return user2 + ' beats ' + user1
        else:
            return user1 + ' beats ' + user2
    else:
        return 'Invalid input'

# asks users for their choices
def play():

    u1 = input('USER1: Rock, Paper, or Scissors?').lower()
    u2 = input('USER2: Rock, Paper, or Scissors?').lower()

# determine the result
    result = outcome(u1, u2)

# print the result
    print(result)
#ask user if they want to continue via while loop, if not then break
while True:
    play()

    choice = input('Play again? (y/n)')

    if choice.lower() != 'y':
        break



