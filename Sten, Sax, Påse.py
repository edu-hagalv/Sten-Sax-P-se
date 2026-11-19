import random as rand
choices = ["sten", "sax", "påse"]
print("Nu ska vi spela Sten, Sax eller Påse,\nJag är Python.exe")

namn_1=input("Ange ditt Användarnamn: ") # Denna linje ska be om användarnan och je möjligheten att skriva in det.
namn_exe="Python.exe" #Datorns namn
while True: # Skapar en while-loop som ska kollar ifall antalet omgångar är ett nummer och fortsätter ifall det stämmer, annars så börjar den om
    antal_omgångar=(input("Ange antal omgångar: "))
    if not antal_omgångar.isdigit():
        print("?\nSkriv ett nummer! INTE en bokstav!")
        print("Försök igen")
    else:
        break

omgångar=0
poäng_1=0
poäng_exe=0


for omgångar in range(1, int(antal_omgångar)+1):   # Verkar så att ett system för antalet omgångar är igång så att man har ett visst antal omgångar på sig och den som har mäst poäng efteråt vinner
    print(f"runda {omgångar}:\n-------------------------------")
    while True:
        val=input("Välj Sten, Sax eller Påse:")
        if val in ["sten", "sax", "påse"]:
            break
        else:
            print("Ogiltig input! Försök igen\n")
            
    alternativ = rand.choice(choices)
    omgångar+=1
    
    if val == alternativ:  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print(f"Båda valde {val}")
        print("Oavgjort\n")
        print("ingen får poäng\n")
        
    elif val=="sten" and alternativ=="sax":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("Sten slår sax")
        print(f"{alternativ}")
        print(f"{namn_1} vinner rundan\n")
        poäng_1+=1
        print(f"{namn_1} har {poäng_1} poäng\n")
        
    elif val=="påse" and alternativ=="sten":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("påse slår sten")
        print(f"{namn_1} vinner rundan\n")
        poäng_1+=1
        print(f"{namn_1} har {poäng_1} poäng\n")
        
    elif val=="sax" and alternativ=="påse":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("Sax slår påse")
        print(f"{namn_1} vinner rundan\n")
        poäng_1+=1
        print(f"{namn_1} har {poäng_1} poäng\n")
    
    elif alternativ=="sten" and val=="sax":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("sten slår sax")
        print(f"{namn_exe} vinner rundan\n")
        poäng_exe+=1
        print(f"{namn_exe} har {poäng_exe} poäng\n")
    
    elif alternativ=="påse" and val=="sten":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("påse slår sten")
        print(f"{namn_exe} vinner rundan\n")
        poäng_exe+=1
        print(f"{namn_exe} har {poäng_exe} poäng\n")
    
    elif alternativ=="sax" and val=="påse":  #kollar valet av spelare och dator och bestämmer vem det är som vinner och utdelar poäng
        print("sax slår påse")
        print(f"{namn_exe} vinner rundan\n")
        poäng_exe+=1
        print(f"{namn_exe} har{poäng_exe} poäng\n")



if poäng_1==poäng_exe:
    print(f"Resultat\n--------------\n{namn_1}: {poäng_1}\n{namn_exe}: {poäng_exe}\n")
    print(f"Matchen blev lika då båda fick {poäng_1} poäng, nästan där")
        
elif poäng_1>poäng_exe:
    print(f"Resultat\n--------------\n{namn_1}: {poäng_1}\n{namn_exe}: {poäng_exe}\n")
    print(f"{namn_1} har {poäng_1} poäng och vinner matchen, Grattis!")
        
elif poäng_1<poäng_exe:
    print(f"Resultat\n--------------\n{namn_1}: {poäng_1}\n{namn_exe}: {poäng_exe}\n")
    print(f"{namn_exe} har {poäng_exe} poäng och vinner matchen, :( Bättre lycka nästa gång.")
    print(f"{namn_exe} har {poäng_exe} poäng och vinner matchen, :( Bättre lycka nästa gång.")
    