import string
def checkStrength(password):

    
    if True: # Storing different types of characters as lists
        chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        charslower = list(string.ascii_lowercase)
        charsupper = list(string.ascii_uppercase)
        charsdigits = list(string.digits)
        charssymbols = list("!@#$%^&*()")
    if True: # Conditions
        lowerCondition = any(charslower in password for charslower in charslower)  
        upperCondition = any(charsupper in password for charsupper in charsupper) 
        digitCondition = any(charsdigits in password for charsdigits in charsdigits) 
        symbolCondition = any(charssymbols in password for charssymbols in charssymbols)
    if True: #Condition counting
        conditionCounter = 0
        if lowerCondition:
            conditionCounter += 1
        if upperCondition:
            conditionCounter +=1
        if digitCondition:
            conditionCounter +=1
        if symbolCondition:
            conditionCounter += 1
    lengthCondition = len(password) >= 7

    # Weak:
    if (conditionCounter == 1 or conditionCounter ==2):
        print('The password strength is: Weak')
    elif ((conditionCounter == 3) or (conditionCounter == 4 and lengthCondition == False)):
        print('The password strength is: Medium')
    else:
        print('The password strength is: Strong')
                    

    

