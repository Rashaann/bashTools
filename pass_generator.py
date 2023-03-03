""" Code created by Zakstein in 01/07/2021 - updated in 28/02/2022
mail : zakaria1712@hotmail.fr
It permit to create random passwords."""

from random import *
import time

#Initialisation des tableaux
special_character = ["&",'"',"'","(","!",")","-","_","$","€","*","£","%","+","=","/",":",".",";",",","?"]
number = ["0","1","2","3","4","5","6","7","8","9"]
ALPHABET = []
alphabet = []

for i in range(65,91):
    ALPHABET.append(chr(i))
for i in range(97, 123):
    alphabet.append(chr(i))





print("\n")
print(
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░\n")+
"\n"
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║\n")+
"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,"░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n"))
time.sleep(0.5)
print("\n")
time.sleep(0.5)
print("\n")
time.sleep(0.5)
print("\n")







pswd = '' #Initialisation du mot de passe

#Choix de la longueur du mot de passe
q1 = 'n'

while(q1 != 'y') :
    N = input("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,'Choose the length of your password : '))
    time.sleep(0.5)
    print('\n')
    q1 = input("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,'The chosen length is ' + str(N) + '.\n' + "Is that right? Select 'y' or 'n' : "))
    time.sleep(0.5)
    print('\n')

N = int(N)
tab_tot = []


#Certains sites ne tolerent pas les caracteres speciaux.
#Les conditions suivantes permettent donc de choisir
#si l'on veut les integrer dans notre mot de passe ou non.
q2 = input("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"Do you want to have special characters in your password? \nSelect 'y' or 'n' : "))
time.sleep(0.5)
print('\n')

if (q2 == 'y') :
    tab_tot = tab_tot + special_character
    tab_tot = tab_tot + number
    tab_tot = tab_tot + ALPHABET
    tab_tot = tab_tot + alphabet
else :
    tab_tot = tab_tot + number
    tab_tot = tab_tot + ALPHABET
    tab_tot = tab_tot + alphabet


#Construction du mot de passe
for i in range(N) :
    pswd = pswd + str(choice(tab_tot))

#Affichage du mot de passe final
print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"The password generated is the one below :\n {}".format("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,pswd))))
time.sleep(0.5)
print('\n')

#La boucle while permet de creer un nouveau de mot de passe
#s'il ne convient pas a l'utilisateur.
final = 'y'

while (final != 'n') :
    final = input("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"If this pass doesn't satisfy you, another one can be generated...\nWould you like to generate a new one? Select 'y' or 'n' : "))
    time.sleep(0.5)
    print('\n')
    
    if (final == 'y') :
        pswd = ''    
        for i in range(N) :
            pswd = pswd + str(choice(tab_tot))
        print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"The password generated is the one below :\n {}".format("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(82, 152, 210,pswd))))
        time.sleep(0.5)
        print('\n')
        final = input("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"If this pass doesn't satisfy you, another one can be generated...\nWould you like to generate a new one? Select 'y' or 'n' : "))
        time.sleep(0.5)
        print('\n')
    else :
        continue


print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(205, 145, 122,"Goodbye then ✋✋"))
