from tkinter import *
import pantilthat

pantilthat.idle_timeout(0.5)

# definir les angles
def Position_TILT(valeur_tilt):
	angle = int(valeur_tilt) / 2
	pantilthat.tilt(angle)	
def Position_PAN(valeur_pan):
	angle = int(valeur_pan) / 2
	pantilthat.pan(angle)
	
# creation fenetres
fenetre1 = Tk()
fenetre2 = Tk()

# personnalisation fenetres
fenetre1.geometry("80x200")
fenetre1.minsize(80, 200)
fenetre1.maxsize(80, 200)
fenetre1.config(background='#41B77F')
fenetre2.title("    ")
fenetre2.geometry("230x50")
fenetre2.minsize(230, 50)
fenetre2.maxsize(230, 50)
fenetre2.config(background='#41B77F')

#Ajout du slide
scale1 = Scale(fenetre1, from_=-90, to=90, orient=VERTICAL, command = Position_TILT, length=200, width=55)
scale1.place(x=0, y=0)
scale2 = Scale(fenetre2, from_=-90, to=90, orient=HORIZONTAL, command = Position_PAN, length=230, width=25)
scale2.place(x=0, y=0)


# afficher fenetre
fenetre1.mainloop()
fenetre2.mainloop()
