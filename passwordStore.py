def passwordStorage():
    from checkStrength import checkStrength # To inform user of MP Strength
    from securityQuestion import securityQuestion # To ask for security answer when resetting password
    
    def createMP(): # Function to create and return master password
        while True:
            while True: # Input and validation of master password
                try:
                    masterpassword = str(getpass('Enter new master password, you will not be able to view it while typing.\n(It is recommended that this be a strong password which you would remember): '))
                    if len(masterpassword) <=0:
                        negativevalueError = ValueError("Can't be less than 0")
                        raise negativevalueError
                    break
            
                except ValueError or TypeError or negativevalueError:
                    print('That is invalid, please try again')
                    continue
            checkStrength(masterpassword)
            while True: # Input and validation of continue check
                try:
                    continueCheck = ((str(input('Do you want to continue? (Y/N)')))).upper()
                    if continueCheck != 'Y' and continueCheck != 'N':
                        print("That is invalid, please enter 'Y' or 'N'")
                        continue
                    break
                except TypeError or ValueError:
                    print("That is invalid, please enter 'Y' or 'N'")
                    continue
            if continueCheck == 'N':
                continue
            elif continueCheck == 'Y':
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
                    break
        return masterpassword
    
    from getpass import getpass # Module to hide input of passwords while typing 
    
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
    
    else: # Main code block to view passwords
        
        validatingAuthenticity = False # Initialise of Bool to check if user knows master password
        
        with open('masterpasswordcheck.txt', 'r') as MPCheck: # Opens masterpassword file to check if it exists and/or create it
                
                firstline = MPCheck.read() #Extracts first line from masterpassword file
                if len(firstline) == 0:    # If master password doesn't exist yet
                        firstline = createMP()
                        with open('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/masterpasswordcheck.txt', 'w') as MPCheck:
                            MPCheck.write(firstline)
                        validatingAuthenticity = True
                        global security
                        security = securityQuestion()
                        with open('securityquestion.txt', 'a+') as securityFile:
                            securityFile.write(security[0] + '\n')
                            securityFile.write(security[1])
                
                # Gets here when master password has been created 
                
                else: # If master password exists, prompts user to enter it or reset it
                    while True:
                        validatingAuthenticity = False
                        print("Enter your master password to continue (Or input 'F' to reset it): ")
                        masterpasswordcheck = str(getpass())
                        if masterpasswordcheck == 'F': # Reseting code block
                            
                            while True: # Input and validation of continue check (Whether user remembers password)
                                try:
                                    rememberCheck = str(input('Do you remember the old password? (Y/N) ')).upper()
                                    if rememberCheck == 'Y' or rememberCheck == 'N':
                                        break
                                    else:
                                        continue
                                except TypeError or ValueError:
                                    print("That is invalid, please enter 'Y' or 'N'")
                                    continue
                            
                            if rememberCheck == 'Y': # User remembers old password, initiate reset
                                while True:
                                    masterpasswordcheck = str(getpass('Enter your old password: (You will not be able to view it while typing) '))
                                    if masterpasswordcheck != firstline:
                                        print('That is wrong, try again')
                                        continue
                                    else:
                                        break
                                with open('masterpasswordcheck.txt', 'r+') as MPCheck:
                                    MPCheck.truncate(0)
                                with open('masterpasswordcheck.txt', 'w') as MPCheck:
                                    firstline = createMP()
                                    MPCheck.write(firstline)
                                security = securityQuestion()
                            
                            else: # User forgot password, ask security question, initiate reset
                                with open('securityquestion.txt', 'r') as SecurityFile:
                                    securitylines = []
                                    for line in SecurityFile:
                                        securitylines.append(line.strip())
                                print('Your secuirty question is: ', securitylines[0])
                                while True:
                                    answer = str(input('Please enter the answer to your security question: '))
                                    if answer != securitylines[1]:
                                        print('That answer is incorrect, please try again:')
                                        continue
                                    else:
                                        break
                                with open('masterpasswordcheck.txt', 'r+') as MPCheck:
                                    MPCheck.truncate(0)
                                with open('masterpasswordcheck.txt', 'w') as MPCheck:
                                    firstline = createMP()
                                    MPCheck.write(firstline)
                                with open('securityquestion.txt', 'r+') as securityFile:
                                    securityFile.truncate(0)
                                    security = securityQuestion()
                                    securityFile.write(security[0] + '\n')
                                    securityFile.write(security[1])
                    
                        elif masterpasswordcheck != firstline: # User doesn't reset, but enters wrong password
                            print('That is invalid, please try again.')
                            continue
                        else: # User enters correct password, break out of the loop and allow access to file
                            validatingAuthenticity = True
                            break
        
        if validatingAuthenticity == True: # Allows user to access passwords generated from passwordGeneration.py
            import os
            fileExist = os.path.exists('file-passwords.txt') # Checks if user has generated at least one password 
            entryExist = os.stat('file-passwords.txt').st_size
            if fileExist == True and entryExist > 0: # Shows the user the passwords and terminates     
               
                with open ('file-passwords.txt', 'r') as myfile: #Extracting number of lines
                    mylines = []
                    noOfLines = len((myfile).readlines())
                myfile.close()
                
                with open ('file-passwords.txt', 'r') as myfile: #Printing two consectuive lines in order to show a complete entry
                    for line in myfile:
                        mylines.append(line.strip())
                    for i in range(0,noOfLines, 2):
                        mylines[i] = mylines[i]
                        mylines[i+1] = mylines[i+1]
                        print('\n',(int((i+2)/2)),': Site and email:\n', mylines[i], '\nPassword:\n', mylines[i+1], sep="")
                
                while True: # Returning to homescreen
                    try:
                        returning = input('Press enter when you would like to return to the homescreen\n')
                        if returning == '':
                            return
                        else:
                            raise ValueError
                    except ValueError:
                        continue
            
            else: # No passwords have been created,terminate program and return to main.py
                while True:
                    try:
                        returning = input("You haven't stored any passwords yet.\nPress enter when you would like to return to the homescreen\n")
                        if returning == '':
                            return
                        else:
                            raise ValueError
                    except ValueError:
                        continue