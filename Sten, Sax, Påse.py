import random as rand
choices = ["sten", "sax", "påse"]
print("Nu ska vi spela Sten, Sax eller Påse,\nJag är Python.exe")

namn_1=input("Ange ditt Användarnamn: ") # Denna linje ska be om användarnan och je möjligheten att skriva in det.
namn_2="Python.exe"
omgång=int(input("Ange antal omgångar: ")) # Denna linje ska be om antalet omgångar.
val=input("Välj Sten, Sax eller Påse: \n")

alternativ = rand.choice(choices)

if val == alternativ:
    print(f"Båda valde {val}")
    print("Oavgjort")
elif val=="sten" and alternativ!="papper":
    print("Sten slår sax")
    print(f"{namn_1} vinner rundan")
elif val=="papper" and alternativ!="sax":
    print("papper slår sten")
    print(f"namn_1 vinner rundan")
elif val=="sax" and alternativ!="sten":
    print("Sax slår papper")
    print(f"{namn_1} vinner rundan")
elif alternativ=="sten" and val!="papper":
    print("sten slår sax")
    print(f"{namn_2} vinner rundan")
elif alternativ=="papper" and val!="sax":
    print("papper slår sten")
    print(f"{namn_2} vinner rundan")
elif alternativ=="sax" and val!="sten":
    print("sax slår papper")
    print(f"{namn_2} vinner rundan")