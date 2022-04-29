from colorama import *
#pip install colorama
from pyttsx3 import *
#pip install pyttsx3
import sys
print(Fore.GREEN + """                                   Welcom to secretLanguge  :)             """)
print(Fore.CYAN + """                                    create by CyberMan                 """)
print(Fore.BLUE + "1.Please Enter messages for Encryption  ")
print(Fore.RED + "2.Please Enter messages for Decryption  ")
print(Fore.MAGENTA + "3.Exit")
print(Fore.YELLOW + "4.about")
SEC=[]
sec1=int(input(Fore.WHITE +"Please select a options >> "))
if sec1==1:
    print(Fore.GREEN + """                            Welcom to unit messages Encryption :)     """)
    print(Fore.RED + "Type 'stop' to end the operation, then press Enter")
    SEC2=input(Fore.BLUE + "Enter your messages for Encryption >> ")
    for KEY in SEC2:
        if KEY=="A":
            SEC3=10
        elif KEY=="B":
            SEC3=11
        elif KEY=="C":
            SEC3=12
        elif KEY=="D":
            SEC3=13
        elif KEY=="E":
            SEC3=14
        elif KEY=="F":
            SEC3=15
        elif KEY=="G":
            SEC3=16
        elif KEY=="H":
            SEC3=17
        elif KEY=="I":
            SEC3=18
        elif KEY=="J":
            SEC3=19
        elif KEY=="K":
            SEC3=20
        elif KEY=="L":
            SEC3=21
        elif KEY=="M":
            SEC3=22
        elif KEY=="N":
            SEC3=23
        elif KEY=="O":
            SEC3=24
        elif KEY=="P":
            SEC3=25
        elif KEY=="Q":
            SEC3=26
        elif KEY=="R":
            SEC3=27
        elif KEY=="S":
            SEC3=28
        elif KEY=="T":
            SEC3=29
        elif KEY=="U":
            SEC3=30
        elif KEY=="V":
            SEC3=31
        elif KEY=="W":
            SEC3=32
        elif KEY=="X":
            SEC3=33
        elif KEY=="Y":
            SEC3=34
        elif KEY=="Z":
            SEC3=35
        elif KEY=="a":
            SEC3=10
        elif KEY=="b":
            SEC3=11
        elif KEY=="c":
            SEC3=12
        elif KEY=="d":
            SEC3=13
        elif KEY=="e":
            SEC3=14
        elif KEY=="f":
            SEC3=15
        elif KEY=="g":
            SEC3=16
        elif KEY=="h":
            SEC3=17
        elif KEY=="i":
            SEC3=18
        elif KEY=="j":
            SEC3=19
        elif KEY=="k":
            SEC3=20
        elif KEY=="l":
            SEC3=21
        elif KEY=="m":
            SEC3=22
        elif KEY=="n":
            SEC3=23
        elif KEY=="o":
            SEC3=24
        elif KEY=="p":
            SEC3=25
        elif KEY=="q":
            SEC3=26
        elif KEY=="r":
            SEC3=27
        elif KEY=="s":
            SEC3=28
        elif KEY=="t":
            SEC3=29
        elif KEY=="u":
            SEC3=30
        elif KEY=="v":
            SEC3=31
        elif KEY=="w":
            SEC3=32
        elif KEY=="x":
            SEC3=33
        elif KEY=="y":
            SEC3=34
        elif KEY=="z":
            SEC3=35
        else:
            print(Fore.RED + "Error please try again")
        SEC.append(SEC3)
    print(SEC)
elif sec1==2:
    print(Fore.GREEN + """                            Welcome to unit messages Decryption :)          """)
    SEC3=" The code was opened >> "
    print(Fore.BLUE + "Type 'stop' to end the operation, then press Enter")
    while True:
        SEC2=input(Fore.RED + "Enter your messages for Decryption >> ")
        SEC.append(SEC3)
        if SEC2=="stop":
            break
        elif SEC2=="10":
            SEC3="A"
        elif SEC2=="11":
            SEC3="B"
        elif SEC2=="12":
            SEC3="C"
        elif SEC2=="13":
            SEC3="D"
        elif SEC2=="14":
            SEC3="E"
        elif SEC2=="15":
            SEC3="F"
        elif SEC2=="16":
            SEC3="G"
        elif SEC2=="17":
            SEC3="H"
        elif SEC2=="18":
            SEC3="I"
        elif SEC2=="19":
            SEC3="J"
        elif SEC2=="20":
            SEC3="K"
        elif SEC2=="21":
            SEC3="L"
        elif SEC2=="22":
            SEC3="M"
        elif SEC2=="23":
            SEC3="N"
        elif SEC2=="24":
            SEC3="O"
        elif SEC2=="25":
            SEC3="P"
        elif SEC2=="26":
            SEC3="Q"
        elif SEC2=="27":
            SEC3="R"
        elif SEC2=="28":
            SEC3="S"
        elif SEC2=="29":
            SEC3="T"
        elif SEC2=="30":
            SEC3="Y"
        elif SEC2=="31":
            SEC3="V"
        elif SEC2=="32":
            SEC3="W"
        elif SEC2=="33":
            SEC3="X"
        elif SEC2=="34":
            SEC3="Y"
        elif SEC2=="35":
            SEC3="Z"
        else:
            print(Fore.BLUE + "Error please try again")
    print(SEC)
elif sec1==3:
    speak("are you sure to Exit?")
    out=input(Fore.MAGENTA + "are you sure to Exit (y/n) >> ")
    if out=="y":
        sys.exit(0)
    else:
        print(Fore.MAGENTA + "Please a restart script :) ")
elif sec1==4:
    print(Fore.YELLOW + """ create by cyberman2020  This script converts the letters of the English alphabet to numbers, for example A, B, C ... replaces the numbers 10, 11 and 12, respectively.
Note: This program is an encryption language """)
speak("create by cyberman2020  This script converts the letters of the English alphabet to numbers, for example A, B, C ... replaces the numbers 10, 11 and 12, respectively.Note: This program is an encryption language ")
