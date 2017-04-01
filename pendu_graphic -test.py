from tkinter import *

essais = 5 
mot = "canvas"  
mot_found = "" 
i = 0 
lettre = 0
found = 0 
longueur = len(mot)
execute = False
lettre_try_str = ""
mot_crypt_str = "" 

if found == 0:
    while i <= (longueur - 1):
        mot_crypt_str = mot_crypt_str + "-"
        i += 1

        
class Interface(Frame):
    def __init__(self, fenetre):
        global j2_mot
        global mot_crypt_str
        global lettre_try_str
        global essais
        global mot_crypt
        global lettre_try
        
        j2_mot = StringVar()
        lettre_try = StringVar()
        mot_crypt = StringVar() 
        
        Frame.__init__(self, fenetre)
        self.pack(fill=BOTH)

        Frame_pendu = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame_pendu.pack(side=LEFT, padx=5, pady=5)

        Frame_stats = LabelFrame(fenetre, text="Statut")
        Frame_stats.pack(side=RIGHT, padx=1, pady=1)

        Frame_entry = LabelFrame(Frame_stats,text="entrée")
        Frame_entry.pack(side=BOTTOM, expand="yes")

        Canvas(Frame_pendu, bg="white", height=472).pack(padx=1,pady=1)
        
        Button(Frame_entry, text ='Valider', command=Execute).pack(side=RIGHT, padx=5, pady=5)

        j2_input = Entry(Frame_entry, textvariable=j2_mot, width=20).pack(side=LEFT, padx=5, pady=5)

        mot_crypt.set(mot_crypt_str)
        label1 = Label(Frame_stats, textvariable=mot_crypt).pack()
        lettre_try.set(lettre_try_str)
        label2 = Label(Frame_stats, textvariable=lettre_try).pack()
        label3 = Label(Frame_stats, textvariable="Essais restants: " + str(essais)).pack()

def Test():
    global execute
    global lettre
    global lettre_str
    global lettre_try
    global lettre_try_str
    global mot_crypt_str
    global essais
    global found
    global j_mot
    global mot_crypt

    mot_crypt_str = mot_crypt.get()
    mot_crypt_str = list(mot_crypt_str)
    lettre_try_str = lettre_try.get()
    lettre_try_str = list(lettre_try_str)

    j_mot = j2_mot.get()
    if mot.find(j_mot) != -1 and execute == True:
        lettre = mot.find(j_mot)
        lettre_str = mot[lettre]
        print(mot_crypt_str)
        del mot_crypt_str[lettre]
        mot_crypt_str.insert(lettre, lettre_str)
        lettre_try_str.append(lettre_str)
        i = 0
            
        print("cette lettre est dans ce mot\n\n")
        essais = 5
        found += 1
        
        mot_crypt_str = str(mot_crypt_str)
        mot_crypt.set(mot_crypt_str)
        lettre_try_str = str(lettre_try_str)
        lettre_try.set(lettre_try_str)
        mot_crypt_str = ""
    else:
        print("cette lettre n'est pas dans le mot")
        lettre_try.append(j_mot)
        essais -= 1
        
        mot_crypt = (mot_crypt)
        lettre_try =(lettre_try)
        
def Execute():
    global execute
    execute = True
    print("bouton pressé")
    Test()

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy()
