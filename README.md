# AliLock: Password Manager
Welcome to my password manager! 

This project is to help me master the basic/amateur data structures in python and how to deal with them.

# passwordGeneration.py
Firstly, a simple password generator which takes an input for the length of the password and generates a password which should
fulfill the requirements of any website-login, which in turn makes every password very secure.

The password generator also asks for the name of the site and the email with which the website is registered with and stores these
details in a text file in two consecutive lines, containing the email and site, and password, respectively. Collectively, the two
lines are know as an entry. When the password is generated, it is copied to the clipboard.

# passwordStore.py
The details in the text file can be accessed using the passwordStore module, which before allowing access, needs a master password,
the user is prompted to enter one the first time they access the module, the password is then stored on one line of a new text file,
each time the user uses this module after the first one, the input is compared with the first line of the text file. 

(Currently the functionality to reset the password is not available.) 

The user is then able to view all the entries in a neat, organized way.


