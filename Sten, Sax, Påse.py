print("Nu ska vi spela Sten, Sax eller Påse,\nJag är Python.exe")

namn=input("Ange ditt Användarnamn: ") # Denna linje ska be om användarnan och je möjligheten att skriva in det.
omgång=int(input("Ange antal omgångar: ")) # Denna linje ska be om antalet omgångar.
val=input("Välj Sten, Sax eller Påse: ")

alternativ = range(1,3)
sten=1
papper=2
sax=3
import random as rand
rand=rand.choice[alternative]
