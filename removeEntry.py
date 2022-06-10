def removeEntry():

    print('\nWelcome to password management')
    while True: # Input and validation of action
        try:
            action = int(input("Enter what you would like to do:\n"
                        '1: Remove a password entry\n'
                        '2: Go back\n'))
            if action < 0:
                negativeError = ValueError('This value is negative')
                raise negativeError
            elif action != 1 and action != 2:
                invalidValueError = ValueError('Not a valid option')
                raise invalidValueError 
            break
        except ValueError or TypeError:
            print('That is invalid, please enter a valid number which corresponds to the options above')
            continue

    if action == 2: # Return dummy value and iterate main.py again
        return ("Exit")
    else: # Main function
        
        print('To remove a password entry, you need to view your passwords\nStarting password storage... ')
        if True: # Collapsing passwordStore code
                from getpass import getpass # Module and its function to hide input while typing. Used on 23, 24 and 37
                print ('\nWelcome to password storage!')
                while True: # Input and validation of action
                    try:
                        action = int(input("Enter what you would like to do:\n"
                                    '1: View your passwords\n'
                                    '2: Go back\n'))
                        if action != 1 and action != 2:
                            invalidValueError = ValueError('Invalid value')
                            raise invalidValueError
                        break
                    except ValueError or TypeError or invalidValueError:
                        print('That is invalid, please enter a valid number which corresponds to the options above')
                        continue
                if action == 2: # Return dummy value and iterate main.py again
                    return ("Exit")
                else:
                    validatingAuthenticity = False # Bool to check that user knows master password
                    with open('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/masterpasswordcheck.txt', 'a+') as MPCheck: # Opens masterpasswordcheck.txt for appending
                        with open('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/masterpasswordcheck.txt', 'r+') as MPCheck: # Opens same file for reading
                            firstline = MPCheck.read() #Extracts first line from file 
                            if len(firstline) == 0:    # If master password doesn't exist yet
                                while True:
                                    while True: # Input and validation of master password
                                        try:
                                            masterpassword = str(getpass('Enter master password for first time, you will not be able to view it while typing.\n(It is recommended that this be a strong password which you would remember): '))
                                            if len(masterpassword) <=0:
                                                negativevalueError = ValueError("Can't be less than 0")
                                                raise negativevalueError
                                            break
                                        except ValueError or TypeError:
                                            print('That is invalid, please try again')
                                            continue
                                    while True: # Input and validation of  confirmation of master password
                                        try:
                                            masterpasswordcheck = str(getpass('Confirm master password (you will not be able to view it while typing): '))
                                            if len(masterpassword) <=0:
                                                negativevalueError = ValueError("Can't be less than 0")
                                                raise negativevalueError
                                            break
                                        except ValueError or TypeError or negativevalueError:
                                            print('That is invalid, please try again')
                                            continue
                                    if True: # Checking if user entered same password both times
                                        if masterpassword != masterpasswordcheck: 
                                            print("They don't match, try again")
                                            continue
                                        else:
                                            MPCheck.write(masterpassword)
                                            firstline = masterpassword
                                            validatingAuthenticity = True
                                            break
                                # Gets here when master password has been created 
                            else: # If master password exists, prompts user to enter it until they get it right
                                while True:
                                    validatingAuthenticity = False
                                    masterpasswordcheck = str(getpass('Enter your master password to continue: '))
                                    if masterpasswordcheck != firstline:
                                        print('That is invalid, please try again.')
                                        continue
                                    else:
                                        validatingAuthenticity = True
                                        break
                    if validatingAuthenticity == True: # Allows user to access passwords generated from passwordGeneration.py
                        import os.path
                        passwordsexist = os.path.exists('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/file-passwords.txt') # Checks if user has generated at least one password 
                        if passwordsexist == True: # Prints two consecutive lines of 'file-passwords.txt' next to each other in the format "n: (site) - (storedpassword) "                            
                            with open ('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/file-passwords.txt', 'r') as myfile: 
                                mylines = []
                                noOfLines = len((myfile).readlines())
                            myfile.close()
                            with open ('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/file-passwords.txt', 'r') as myfile: 
                                for line in myfile:
                                    mylines.append(line.strip())
                                for i in range(0,noOfLines, 2):
                                    mylines[i] = mylines[i]
                                    mylines[i+1] = mylines[i+1]
                                    print('\n',(int((i+2)/2)),': Site and email:\n', mylines[i], '\nPassword:\n', mylines[i+1], sep="")
                            myfile.close()
                            while True: # Entering which entry to remove
                                try:
                                    removedEntry = int(input('Enter the number of the entry you would like to remove: '))
                                    if removedEntry > (noOfLines/2):
                                        EntryError = ValueError('That is an invalid entry value')
                                        raise EntryError
                                    break
                                except ValueError or TypeError or EntryError:
                                    print('Invalid entry, try again')
                                    continue
                        else:
                            while True: # If no passwords exist yet, terminate and return to main.py
                                try:
                                    returning = input("You haven't stored any passwords yet.\nPress enter when you would like to return to the homescreen\n")
                                    if returning == '':
                                        return('')
                                    else:
                                        raise ValueError
                                except ValueError:
                                    continue                   
        
        with open('file-passwords.txt', 'r') as passwords: # Removing entry by iterating file and keeping all other entries
            lines = passwords.readlines()
            pointer = 1
            with open('file-passwords.txt', 'w') as passwordWrite:
                for line in lines:
                    if removedEntry == 1:
                        if pointer != 1 and pointer != 2:
                            passwordWrite.write(line)
                        pointer += 1
                    elif removedEntry != 1:
                        if (pointer != ((removedEntry*2))) and (pointer != (removedEntry*2)-1):
                            passwordWrite.write(line)
                        pointer +=1
                print('Entry ', removedEntry, 'has been removed!')

        while True: # Returning to homescreen
            try:
                returning = input("Press enter when you would like to return to the homescreen\n")
                if returning == '':
                    return('')
                else:
                    raise ValueError
            except ValueError:
                continue       