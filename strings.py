import os

def greetingString():
    os.system("CLS")
    print('\t-------------------------------------------------- ')
    print("\t  Welcome to the automatic modify images program ")
    print('\t-------------------------------------------------- ')

def menuString():
    print('  -------------------------------------------------------------- ')
    print('\t\tMenu - Please choose an option')
    print('\t\t  Only numbers are accepted')
    print('  -------------------------------------------------------------- ')
    print('  >\t\tPaso #1. Escoger la cantidad de imagenes       <')
    print('  >\t\tPaso #2. Modificar las imagenes\t\t       <')
    print('  >\t\tPaso #3. Ingresar el correo destinatario       <')
    print('  >\t\tPaso #4. Salir\t\t\t\t       <')
    print('  -------------------------------------------------------------- \n')

def inputErrorString():
    print('  ------------------------------------------------- ')  
    print('>      INPUT ERROR: Only numbers are allowed       <')
    print('  ------------------------------------------------- ')
    os.system("PAUSE")

def newUserString():
    os.system("CLS")
    print('  ------------------------------------------------- ')
    print("           You have chosen to input a new user ")
    print("          Please fill the following information")
    print('  ------------------------------------------------- ')