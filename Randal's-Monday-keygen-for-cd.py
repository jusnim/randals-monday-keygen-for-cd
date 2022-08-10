from tkinter import StringVar, OptionMenu
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

#needed Variables
tubeklebstoff = ["1", "1815", "0550", "5308", "9805", "1287", "4039", "2219"]
hasenpfote = ["2","5578","1183","3883","9475","5495","3010","7021"]
geld = ["3","8569","5300","9746","8208","3716","6593","4051"]
Nikotinkaugummi = ["4","9868","5616","8591","3781","8229","3633","1611"]
Miniatur = ["5","2755","4399","9821","6005","7643","5866","9084"]
hotdog = ["6","8719","1452","5070","8611","8563", "2138","2241"]
rostigeklinge = ["7","7668","3861","9919","5326","6198","3983","2371"]
molotovcocktail = ["8","6172","1624","4349","2063","8197","4498","6774"]
ring = ["9","9524","1448","9647","2367","1608","2081","0341"]
eukalyptusbonbon = ["10","0078","9294","5964","5645","6624","5833","9731"]
Brecheisen = ["11","1681","1230","0686","8959","7936","7359","6157"]
limo = ["12","4813","2139","4187","7827","9365","5858","5678"]

Chronojohn = ["1", "0"]
timeportal = ["2", "7"]
tardis = ["3", "1"]
delorean = ["4", "4"]
toaster = ["5", "5"]
phonebooth = ["6", "3"]
timemachine = ["7", "9"]

sally = 0
derdieb = 1
charlie = 2
sgtKramer = 3
mortimer = 4
mrmarconi = 5
sleazy = 6
Mel = 7
Murray = 8
Penner = 9
Matt = 10
Randal = 11

#UI
margin = 5
picwidth= 100

windowwidth = 9*picwidth + 18*margin + 10*margin
windowheight = int((windowwidth / 6) * 2)

window = tk.Tk()

window.geometry(str(windowwidth) + "x" + str(windowheight))



psally = ImageTk.PhotoImage((Image.open(".\Personen/Sally.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pderdieb = ImageTk.PhotoImage((Image.open(".\Personen/derdieb.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pcharlie = ImageTk.PhotoImage((Image.open(".\Personen/charlie.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
psgtKramer = ImageTk.PhotoImage((Image.open(".\Personen/sgt. Kramer.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pmortimer = ImageTk.PhotoImage((Image.open(".\Personen/mortimer.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pmrmarconi = ImageTk.PhotoImage((Image.open(".\Personen/mr. marconi.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
psleazy = ImageTk.PhotoImage((Image.open(".\Personen/sleazy.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pMel = ImageTk.PhotoImage((Image.open(".\Personen/Mel.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pMurray = ImageTk.PhotoImage((Image.open(".\Personen/Murray.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
#pPenner = ImageTk.PhotoImage((Image.open(".\Personen/Penner.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pMatt = ImageTk.PhotoImage((Image.open(".\Personen/Matt.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pRandal = ImageTk.PhotoImage((Image.open(".\Personen/Randal.png")).resize((picwidth, picwidth), Image.ANTIALIAS))

ptubeklebstoff = ImageTk.PhotoImage((Image.open(".\items/Tube Klebstoff.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
phasenpfote = ImageTk.PhotoImage((Image.open(".\items/hasenpfote.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pgeld = ImageTk.PhotoImage((Image.open(".\items/geld.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pNikotinkaugummi = ImageTk.PhotoImage((Image.open(".\items/Nicotine Gum.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pMiniatur = ImageTk.PhotoImage((Image.open(".\items/Miniatur.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
photdog= ImageTk.PhotoImage((Image.open(".\items/hotdog.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
prostigeklinge = ImageTk.PhotoImage((Image.open(".\items/rostige Rasierklinge.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
#pmolotovcocktail = ImageTk.PhotoImage((Image.open(".\items/molotovcocktail.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pring = ImageTk.PhotoImage((Image.open(".\items/ring.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
peukalyptusbonbon = ImageTk.PhotoImage((Image.open(".\items/eukalyptusbonbon.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
pbrecheisen = ImageTk.PhotoImage((Image.open(".\items/Brecheisen.png")).resize((picwidth, picwidth), Image.ANTIALIAS))
plimo = ImageTk.PhotoImage((Image.open(".\items/limo.png")).resize((picwidth, picwidth), Image.ANTIALIAS))


window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)



choosed_person = StringVar()
choosed_item = StringVar()

def changecolor(x):
    labelx = "label" + str(x)
    globals()[labelx].configure(relief="sunken", bg="slateblue1")

    for i in range(1, 13):
        if (i != x) and (i != 10):
            labeli = "label" + str(i)
            globals()[labeli].configure(bg="ivory2", relief="groove")

    
    choosed_person.set(x)
    


def changecolori(x):
    itemx = "item" + str(x)
    globals()[itemx].configure(relief="sunken", bg="slateblue1")

    for i in range(1, 13):
        if (i != x) and (i != 8):
            itemi = "item" + str(i)
            globals()[itemi].configure(bg="ivory2", relief="groove")
    
    choosed_item.set(x)

def get_code():
    personx = choosed_person.get()
    person = selected_person(int(personx))
    device = clicked.get()
    targetbubblex = choosed_item.get()
    targetbubble = selected_item(int(targetbubblex))
    #print(device)
    #print(targetbubble)
    

    show_code(person, device,targetbubble)


def selected_person(x):
    if x == 1:
        return sally
    elif x == 2:
        return derdieb
    elif x == 3:
        return charlie
    elif x == 4:
        return sgtKramer
    elif x == 5:
        return mortimer
    elif x == 6:
        return mrmarconi
    elif x == 7:
        return sleazy
    elif x == 8:
        return Mel
    elif x == 9:
        return Murray
    elif x == 10:
        return Penner
    elif x == 11:
        return Matt
    elif x == 12:
        return Randal


def selected_item(x):
    if x == 1:
        return tubeklebstoff
    elif x == 2:
        return hasenpfote
    elif x == 3:
        return geld
    elif x == 4:
        return Nikotinkaugummi
    elif x == 5:
        return Miniatur
    elif x == 6:
        return hotdog
    elif x == 7:
        return rostigeklinge
    elif x == 8:
        return molotovcocktail
    elif x == 9:
       return ring
    elif x == 10:
        return eukalyptusbonbon
    elif x == 11:
        return Brecheisen
    elif x == 12:
        return limo




def show_code(person, device,targetbubble):
    print(person)
    print(targetbubble)
    print(int(globals()[device][1]))
    if int(targetbubble[0]) > (person + 1):
        move = (int(targetbubble[0]) - int(tubeklebstoff[0])) - person
    elif int(targetbubble[0]) < (person + 1):
        move = 12 - person + (int(targetbubble[0]) - int(tubeklebstoff[0]))
    else:
        move = 0
   
    keyarrayn = int(globals()[device][1]) + move
    
    if keyarrayn > 12:
        keyarrayn = keyarrayn - 11
    else:
        keyarrayn = keyarrayn + 1

    def switch_mit_if(keyarrayn):
        if keyarrayn == 1:
            return tubeklebstoff[int(globals()[device][0])]
        elif keyarrayn == 2:
            return hasenpfote[int(globals()[device][0])]
        elif keyarrayn == 3:
            return geld[int(globals()[device][0])]
        elif keyarrayn == 4:
            return Nikotinkaugummi[int(globals()[device][0])]
        elif keyarrayn == 5:
            return Miniatur[int(globals()[device][0])]
        elif keyarrayn == 6:
            return hotdog[int(globals()[device][0])]
        elif keyarrayn == 7:
            return rostigeklinge[int(globals()[device][0])]
        elif keyarrayn == 8:
            return molotovcocktail[int(globals()[device][0])]
        elif keyarrayn == 9:
            return ring[int(globals()[device][0])]
        elif keyarrayn == 10:
            return eukalyptusbonbon[int(globals()[device][0])]
        elif keyarrayn == 11:
            return Brecheisen[int(globals()[device][0])]
        elif keyarrayn == 12:
            return limo[int(globals()[device][0])]
        else:
            return 'error'

    print(switch_mit_if(keyarrayn))
    
    codelabel = tk.Label(text="Code " + switch_mit_if(keyarrayn), font=('Helvetica bold', int(picwidth/10)))
    codelabel.grid(row=2, column=4,padx=margin2, pady=margin2)





label1 = tk.Button(image=psally, bg="ivory2", relief="groove", command=lambda: changecolor(1))
label2 = tk.Button(image=pderdieb, bg="ivory2", relief="groove", command=lambda: changecolor(2))
label3 = tk.Button(image=pcharlie, bg="ivory2", relief="groove", command=lambda: changecolor(3))
label4 = tk.Button(image=psgtKramer, bg="ivory2", relief="groove", command=lambda: changecolor(4))
label5 = tk.Button(image=pmortimer, bg="ivory2", relief="groove", command=lambda: changecolor(5))
label6 = tk.Button(image=pmrmarconi, bg="ivory2", relief="groove", command=lambda: changecolor(6))
label7 = tk.Button(image=psleazy, bg="ivory2", relief="groove", command=lambda: changecolor(7))
label8 = tk.Button(image=pMel, bg="ivory2", relief="groove", command=lambda: changecolor(8))
label9 = tk.Button(image=pMurray, bg="ivory2", relief="groove", command=lambda: changecolor(9))
#label10 = tk.Button(image=pPenner, bg="ivory2", relief="groove", command=lambda: changecolor(10))
label11= tk.Button(image=pMatt, bg="ivory2", relief="groove", command=lambda: changecolor(11))
label12 = tk.Button(image=pRandal, bg="ivory2", relief="groove", command=lambda: changecolor(12))

label1.grid(row=0, column=0, padx=margin, pady=margin)
label2.grid(row=0, column=1, padx=margin, pady=margin)
label3.grid(row=0, column=2, padx=margin, pady=margin)
label4.grid(row=0, column=3, padx=margin, pady=margin)
label5.grid(row=1, column=0, padx=margin, pady=margin)
label6.grid(row=1, column=1, padx=margin, pady=margin)
label7.grid(row=1, column=2, padx=margin, pady=margin)
label8.grid(row=1, column=3, padx=margin, pady=margin) 
label9.grid(row=2, column=0, padx=margin, pady=margin)
#label10.grid(row=2, column=1, padx=margin, pady=margin)
label11.grid(row=2, column=2, padx=margin, pady=margin)
label12.grid(row=2, column=3, padx=margin, pady=margin)






item1 = tk.Button(image=ptubeklebstoff, bg="ivory2", relief="groove", command=lambda: changecolori(1))
item2 = tk.Button(image=phasenpfote, bg="ivory2", relief="groove", command=lambda: changecolori(2))
item3 = tk.Button(image=pgeld, bg="ivory2", relief="groove", command=lambda: changecolori(3))
item4 = tk.Button(image=pNikotinkaugummi, bg="ivory2", relief="groove", command=lambda: changecolori(4))
item5 = tk.Button(image=pMiniatur, bg="ivory2", relief="groove", command=lambda: changecolori(5))
item6 = tk.Button(image=photdog, bg="ivory2", relief="groove", command=lambda: changecolori(6))
item7 = tk.Button(image=prostigeklinge, bg="ivory2", relief="groove", command=lambda: changecolori(7))
#item8 = tk.Button(image=pmolotovcocktail, bg="ivory2", relief="groove", command=lambda: changecolori(8))
item9 = tk.Button(image=pring, bg="ivory2", relief="groove", command=lambda: changecolori(9))
item10 = tk.Button(image=peukalyptusbonbon, bg="ivory2", relief="groove", command=lambda: changecolori(10))
item11= tk.Button(image=pbrecheisen, bg="ivory2", relief="groove", command=lambda: changecolori(11))
item12 = tk.Button(image=plimo, bg="ivory2", relief="groove", command=lambda: changecolori(12))


item1.grid(row=0, column=6, padx=margin, pady=margin) 
item2.grid(row=0, column=7, padx=margin, pady=margin) 
item3.grid(row=0, column=8, padx=margin, pady=margin) 
item4.grid(row=0, column=9, padx=margin, pady=margin) 
item5.grid(row=1, column=6, padx=margin, pady=margin) 
item6.grid(row=1, column=7, padx=margin, pady=margin) 
item7.grid(row=1, column=8, padx=margin, pady=margin) 
#item8.grid(row=1, column=9, padx=margin, pady=margin) 
item9.grid(row=2, column=6, padx=margin, pady=margin) 
item10.grid(row=2, column=7, padx=margin, pady=margin) 
item11.grid(row=2, column=8, padx=margin, pady=margin) 
item12.grid(row=2, column=9, padx=margin, pady=margin) 






margin2 = margin *2

space1= tk.Label(bg="ivory2")
space2= tk.Label(bg="ivory2")
space3= tk.Label(bg="ivory2")
space4= tk.Label(bg="ivory2")
space5= tk.Label(bg="ivory2")
space6= tk.Label(bg="ivory2")


options = [
    "Chronojohn",
    "timeportal",
    "tardis",
    "delorean",
    "toaster",
    "phonebooth",
    "timemachine"
]
clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(window, clicked, *options)
drop.config(bg='ivory2', width=margin*2)
drop.grid(row=0, column=4,padx=margin2, pady=margin2)







getcode = tk.Button(window, text='Get code',font=('Helvetica bold',int(picwidth/10)), command=get_code, width=margin*2,bg='brown',fg='white')
getcode.grid(row=1, column=4, padx=margin2, pady=margin2) 


window.mainloop()