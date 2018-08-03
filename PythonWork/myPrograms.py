# -*- coding: utf-8 -*-
import os
import datetime
import random
from battleship import game
from encryptMain import *

class myPrograms:

    def joira():
        newNote = ''

        with open('todo.txt') as b:
            newNote = b.read()
        with open('joira.txt', 'a') as f:
            f.write(str(datetime.datetime.now())+"\n")
            f.write(newNote+"\n\n")
        temp = input("\nAddition successful, Would you like to open the file?\n")
        if temp.lower() == "yes":
            os.startfile('file.txt')
        temp = input("\nPress enter to return...")

    def keygen():
        print("\n")
        keygen = ""
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        length = input("How long? ")
        for x in range(int(length)):
            temp = random.randint(0,71)
            keygen = keygen + alphabet[temp:(temp+1)]
        print(keygen)
        print("\n")

    def battleship():
        game.startGame()

    def encryption():
        encryptionMain.open()
