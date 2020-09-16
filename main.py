import slugify

listeLettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "-"," "]
clef = int(input("\033[91m [+] \033[96mSaisissez la clef : "))

while clef > 26:
    clef -= 26

phrase = (input("\033[91m [+] \033[96mVotre message : ")).lower()
phrase = slugify.slugify(phrase)
phraseCode = []
phrase = phrase.split()


for mot in phrase:
    listeMot = []
    for lettre in mot:
        i = listeLettre.index(lettre)
        if i == 26:
          listeMot.append(listeLettre[27])
        else:
            i -= 26
            if i == 26:
              listeMot.append(listeLettre[27])
            else:
              d7 = (i + clef) % 26
              listeMot.append(listeLettre[d7 - 1])
    phraseCode.append("".join(listeMot))
  
print(" ".join(phraseCode))