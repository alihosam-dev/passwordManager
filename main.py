import os
def clear_console(): # Clearing function to clean up terminal
    os.system('clear')
while True:
    clear_console()
    if True: # Print statements for opening
        print(" Hello and welcome to Ali's password manager!\n")
        print('Here are the available features:\n ')
        print('1: Generate a password for a new account\n'
            '2: View your currently stored passwords\n'
            '3: Remove a password entry\n'
            '4: Exit')
    while True: # Input and validation of 'action'
        try:
            action = int(input('Please enter what you would like to do: '))
            if action < 0:
                negativeError = ValueError('This value is negative')
                raise negativeError
            elif action != 1 and action != 2 and action != 3 and action !=4:
                invalidValueError = ValueError('Not a valid option')
                raise invalidValueError 
            break
        except ValueError:
            print('That is invalid, please enter a valid number corresponding to one of the actions above')
            clear_console
            continue
    clear_console()
    if action == 1: # Call PasswordGenerator function 
        from passwordGeneration import PasswordGenerator    
        functiongenerate = PasswordGenerator()
        if functiongenerate == 'Exit':
            continue
    elif action == 2: # Call passwordStorage function 
        from passwordStore import passwordStorage
        functionstore = passwordStorage()
        if functionstore == 'Exit':
            continue
    elif action ==3: # Call removeEntry function
        from removeEntry import removeEntry
        functionstore = removeEntry()
        if functionstore == 'Exit':
            continue
    else:
        break

print('Thank you for using my password manager, see you next time!')