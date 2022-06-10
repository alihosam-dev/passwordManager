def securityQuestion():
    print('You need to set a security question. Choose from the following list.')
    questions = [
        'What city were you born in?', 'What is your oldest sibling’s middle name?', 'In what city or town did your parents meet?', 'What was your childhood nickname?', 'What is the name of your favorite childhood friend?'
        ]
    print('1. What city were you born in?')
    print('2. What is your oldest sibling’s middle name?')
    print('3. In what city or town did your parents meet?')
    print('4. What was your childhood nickname?')
    print('5. What is the name of your favorite childhood friend?')
    while True: # Input and validation of 'action'
        try:
            action = int(input('Please enter the number of the security question: '))
            if action < 1 or action >5:
                print('That is invalid, please enter a valid number corresponding to one of the actions above')
                continue
            break
        except ValueError or TypeError:
            print('That is invalid, please enter a valid number corresponding to one of the actions above')
            continue
    userQuestion = questions[action-1]
    while True: # Input and validation of answer
        try:
            answer = str(input('Enter the answer to the question you chose: '))
            break
        except ValueError or TypeError:
            print('That is invalid, try again')
            continue
    security = [userQuestion, answer]
    return security