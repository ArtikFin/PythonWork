import string
import pyperclip
import os
from PIL import Image


"""
Serafin's Encryption Program: Version 0.0.5ish
-Functionality at this point: encrypt/decrypt of text, image, encrypt of copypasta
-Goals: copypasta decrypt, gif, all image types, videos, email funcitonality, github upload
ADDITIONS IN VERIONS
0.0.5   7/5/2018    Serafin    Cleaning up the code to be readable and editable

"""
class encryptionMain:
    version = "0.0.5ish"
    def open():
        print("****************************************************************")
        print("Serafin's Encryption Program: Version "+encryptionMain.version+".")
        print("****************************************************************")
        encryptionMain.mainMenu()
    def mainMenu():
        while True:
            print("\nCurrent Functional Modes\n\n(T) - Text Encryption/Decryption\n(I) - Image Encryption/Decryption\n(C) - CopyPasta Encryption\n(E) - Exit\n")
            a =input("")
            if a.lower() == "t":
                encryptionText.menu()
            elif a.lower() == "i":
                encryptionImages.menu()
            elif a.lower() == "c":
                encryptionCopy.menu()
            elif a.lower() == "e":
                break
            else:
                print("\nThat was not a valid answer, try again")

class encryptionText:
    def menu():
        while True:
            print("\nCurrently Available Tasks for Text:\n")
            print("(E) - Encrypt text file\n(D) - Decrypt text file\n(EXIT) - Exit\n")
            a = input("")
            if a.lower() == "e":
                encryptionText.encrypt()
            elif a.lower() == "d":
                encryptionText.decrypt()
            elif a.lower() == "exit":
                break
            else:
                print("\nThat was not a valid answer, try again")
    def encrypt():
        file = input("File name: ")
        encryptWord = input("Encryption Key: ")
        f = open(file,"r")
        fileBefore = f.read()
        fileAfter = ""
        alphabet = string.printable
        for n in range(len(fileBefore)):
            modulo = (n)%(len(encryptWord))
            postIndex = (alphabet.index(fileBefore[n]) + alphabet.index(encryptWord[modulo]))%len(alphabet)
            fileAfter+=alphabet[postIndex]
            #print("Key Index = "+str(modulo)+"; Character index: "+str(n)+"; Alphabet Index: "+str(postIndex))
        g = open(encryptWord,"w")
        g.write(fileAfter)
        g.close()
        b = input("\nEncryption Successful, would you like to delete the old file(Y/N)?")
        if b.lower == "y":
            os.remove(file)
            print("\nFile removed")
    def decrypt():
        file = input("File name: ")
        encryptWord = input("Encryption Key: ")
        f = open(file,"r")
        fileBefore = f.read()
        fileAfter = ""
        alphabet = string.printable
        for n in range(len(fileBefore)):
            modulo = (n)%(len(encryptWord))
            postIndex = (alphabet.index(fileBefore[n]) - alphabet.index(encryptWord[modulo]))%len(alphabet)
            fileAfter+=alphabet[postIndex]
        g = open((file+" decrypted.txt"),"w")
        g.write(fileAfter)
        g.close()
        b = input("\nDecryption Successful, would you like to delete the old file(Y/N)?")
        os.startfile(file+" decrypted.txt")
        if b.lower == "y":
            os.remove(file)
            print("\nFile removed")
        b = input("\nWould you like to delete the text(Y/N)?")
        if b.lower == "y":
            os.remove(file+" decrypted.txt")
            print("\nFile removed")

class encryptionImages:
    def menu():
        while True:
            print("\nCurrently Available Tasks for Imagery:\n")
            print("(E) - Encrypt png file\n(D) - Decrypt png file\n(EXIT) - Exit\n")
            a = input("")
            if a.lower() == "e":
                encryptionImages.encrypt()
            elif a.lower() == "d":
                encryptionImages.decrypt()
            elif a.lower() == "exit":
                break
            else:
                print("\nThat was not a valid answer, try again")
    def encrypt():
        file = input("File name: ")
        encryptWord = input("Encryption key: ")
        f = Image.open(file)
        width, height = f.size
        mode = f.mode
        fileBefore = str(f.tobytes())
        fileAfter = "({},{},'{}')".format(width,height,mode)
        alphabet = string.printable
        for n in range(len(fileBefore)):
            modulo = (n)%(len(encryptWord))
            postIndex = (alphabet.index(fileBefore[n]) + alphabet.index(encryptWord[modulo]))%len(alphabet)
            fileAfter+=alphabet[postIndex]
            #print("Key Index = "+str(modulo)+"; Character index: "+str(n)+"; Alphabet Index: "+str(postIndex))
        g = open(encryptWord,"w")
        g.write(fileAfter)
        b = input("\nEncryption Successful, would you like to delete the old file(Y/N)?")
        if b.lower == "y":
            os.remove(file)
            print("\nFile removed")
    def decrypt():
        file = input("File name: ")
        encryptWord = input("Encryption key: ")
        f = open(file,"r")
        fileBefore = f.read()
        metadata = eval(fileBefore[:fileBefore.index(')')+1])
        print(metadata)
        fileBefore = fileBefore[fileBefore.index(')')+1:]
        fileAfter = ""
        alphabet = string.printable
        for n in range(len(fileBefore)):
            modulo = (n)%(len(encryptWord))
            postIndex = (alphabet.index(fileBefore[n]) - alphabet.index(encryptWord[modulo]))%len(alphabet)
            fileAfter+=alphabet[postIndex]
        fileAfter = Image.frombytes(metadata[2],(metadata[0],metadata[1]),eval(fileAfter))
        fileAfter.save(file+" decrypted.png")
        print("\nDecryption Successful")
        b = input("\nDecryption Successful, would you like to delete the old file(Y/N)?")
        os.startfile(file+" decrypted.png")
        if b.lower == "y":
            os.remove(file)
            print("\nFile removed")
        b = input("\nWould you like to delete the image(Y/N)?")
        if b.lower == "y":
            os.remove(file+" decrypted.png")
            print("\nFile removed")

class encryptionCopy:
    def menu():
        while True:
            print("\nCurrently Available Tasks for CopyPasta:\n")
            print("(E) - Encrypt copied text\n(D) - Decrypt text file (Coming Soon)\n(EXIT) - Exit\n")
            a = input("")
            if a.lower() == "e":
                encryptionCopy.encrypt()
            elif a.lower() == "d":
                encryptionCopy.decrypt()
            elif a.lower() == "exit":
                break
            else:
                print("\nThat was not a valid answer, try again")
    def encrypt():
        encryptWord = input("Encryption Key: ")
        fileBefore = pyperclip.paste()
        fileAfter = ""
        alphabet = string.printable
        for n in range(len(fileBefore)):
            modulo = (n)%(len(encryptWord))
            postIndex = (alphabet.index(fileBefore[n]) + alphabet.index(encryptWord[modulo]))%len(alphabet)
            fileAfter+=alphabet[postIndex]
            #print("Key Index = "+str(modulo)+"; Character index: "+str(n)+"; Alphabet Index: "+str(postIndex))
        g = open(encryptWord,"w")
        g.write(fileAfter)
        g.close()
        print("\nEncryption Successful")
    def decrypt():
        a = input("Sorry, this feature is not available yet.\n\n Press ENTER to return")
