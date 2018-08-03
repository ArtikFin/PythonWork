import sys
import getpass
from myPrograms import myPrograms

currentProgamList = "\n\n-Joira\n-Keygen\n-Battleship\n-Encryption\n-Exit\n\n"

attemptsLeft = 3
cannotAnswer= True
while cannotAnswer== True:
    x = getpass.getpass("PASSWORD REQUIRED: ")
    if x == "ahoymiboi":
        cannotAnswer= False
    else:
        attemptsLeft -= 1
        print("Incorrect Response, "+str(attemptsLeft)+" tries remaining.")
        if attemptsLeft == 0:
            sys.exit("Goodbye")
while True:
    x = input("Which program would you like to run?"+currentProgamList)
    if x.lower() == "joira":
        myPrograms.joira()
    elif x.lower() == "keygen":
        myPrograms.keygen()
    elif x.lower() == "battleship":
        myPrograms.battleship()
    elif x.lower() == "encryption":
        myPrograms.encryption()
    elif x.lower() == "exit":
        sys.exit()
    else:
        print("Program not recognized.")
