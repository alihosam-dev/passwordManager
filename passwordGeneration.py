import random, time, pyperclip, string

def PasswordGenerator():
    print ('\nWelcome to the Password generator')

    while True: # Input and validation of action
        try:
            action = int(input("Enter what you would like to do:\n"
                        '1: Generate a password\n'
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
    elif action == 1: # Main Code for this function
        if True: # Storing different types of characters as lists
            chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
            charslower = list(string.ascii_lowercase)
            charsupper = list(string.ascii_uppercase)
            charsdigits = list(string.digits)
            charssymbols = list("!@#$%^&*()")

        while True: # Input and validation of 'site'
            try:
                site = str(input('Enter the name of the website for which this password is for: '))
                if len(site) <=0:
                    lengthError = ValueError('It cannot be less than 4 characters')
                    raise lengthError
                break
            except ValueError or TypeError or lengthError:
                print('That is invalid, please enter a valid name')
                continue
       
        while True: # Input and validation of 'email'
            if True: # Email validation conditions function
                import re
                def solve(s):
                    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
                    if re.match(pat,s):
                        return True
                    return False    
            try:
                email = str(input('Enter the email for the website you registered an account for: '))
                if len(email) <=0:
                    lengthError = ValueError('It cannot be less than 4 characters')
                    raise lengthError
                emailvalidate = solve(email)
                if emailvalidate == False:
                    validateError  = ValueError('Please enter a valid email')
                    raise validateError
                break
            except ValueError or TypeError or lengthError or validateError:
                print('That is invalid, please enter a valid email')
                continue
        
        while True: # Input and validation of 'length' of password
            try:
                length = int(input("Enter the length of the password \n(Must be greater than or equal to 4 characters and less than 128, we recommend at least 9 for maximum security): "))
                if length <= 4 or length >128:
                    lengthError = ValueError('It cannot be less than 4 characters')
                    raise lengthError
                break
            except ValueError or TypeError or lengthError:
                print('That is invalid')

        print('Generating...')
        time.sleep(0.2)

        while True: # Generating Password with all requirements
            random.shuffle(chars)
            password = []
            for i in range(length):
                password.append(random.choice(chars))
            random.shuffle(password)
            password = "".join(password)
            if True: # Condition for accepting password
                condition = any(charslower in password for charslower in charslower) and any(charsupper in password for charsupper in charsupper) and any(charsdigits in password for charsdigits in charsdigits) and any(charssymbols in password for charssymbols in charssymbols)
            if condition == False:
                continue
            else:
                break

        print('The password is', password) # Printing password to user
        pyperclip.copy(password) #Copying password to clipboard
        print('Password copied to clipboard!')

        if True: #Storing entry in text file
            with open('/Users/alihosam/Ali/Coding/Python Programs/passwordManager/file-passwords.txt', 'a+') as textFile: #Opening/Creating 'file-passwords.txt'
                textFile.write(site + ' - ' + email + '\n') # Storing the site and email first line in file
                textFile.write(password + '\n') # Storing password of site on the next line

    time.sleep(3) # Cool down before returning to main.py
    while True: # Returning to homescreen
        try:
            returning = input('Press enter when you would like to return to the homescreen\n')
            if returning == '':
                return
            else:
                raise ValueError
        except ValueError:
            continue


