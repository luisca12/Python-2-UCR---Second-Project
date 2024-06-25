import os

def greetingString():
    """
    This function clears the console and prints a welcome message for the automatic modify images program.

    **Args:**
        
    **Returns:**
    """
    os.system("CLS")
    print('\t-------------------------------------------------- ')
    print("\t  Welcome to the automatic modify images program ")
    print('\t-------------------------------------------------- ')

def menuString():
    """
    This function prints the menu options for the program.

    **Args:**
        
    **Returns:**
    """
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
    """
    This function prints an error message when an invalid input is detected and pauses the system.

    **Args:**
        
    **Returns:**
    """
    print('  ------------------------------------------------- ')  
    print('>      INPUT ERROR: Only numbers are allowed       <')
    print('  ------------------------------------------------- ')
    os.system("PAUSE")