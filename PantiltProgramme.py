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
	
# creation fenetre
fenetre = Tk()

# personnalisation fenetres
fenetre.geometry("700x400")
fenetre.minsize(100, 100)
fenetre.maxsize(1000, 1000)
fenetre.config(background='#41B77F')


#Ajout du slide
scale1 = Scale(fenetre, from_=-90, to=90, orient=VERTICAL, command = Position_TILT, length=200, width=25)
scale1.place(x=0, y=0)
scale2 = Scale(fenetre, from_=-90, to=90, orient=HORIZONTAL, command = Position_PAN, length=230, width=25)
scale2.place(x=55, y=0)


# afficher fenetre
fenetre.mainloop()

