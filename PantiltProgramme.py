from tkinter import *
import pantilthat

pantilthat.idle_timeout(0.5)

# definir les angles
def mvt_D():
	pantilthat.pan(-20)
	
def mvt_G():
	pantilthat.pan(20)
	
def mvt_H():
	pantilthat.tilt(-35)
	
def mvt_B():
	pantilthat.tilt(35)
	
# creation fenetre
fenetre = Tk()

# personnalisation fenetre
fenetre.title("Orientation camera")
fenetre.geometry("480x360")
fenetre.minsize(480, 360)
fenetre.config(background='#41B77F')

# creation des frames
frame1 = Frame(fenetre, bg='#41B77F')
frame2 = Frame(fenetre, bg='#41B77F')
frame3 = Frame(fenetre, bg='#41B77F')
frame4 = Frame(fenetre, bg='#41B77F')

# ajout de boutons
mv_bouttonD = Button(frame1, text="D", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_D)
mv_bouttonD.pack()
mv_bouttonG = Button(frame2, text="G", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_G)
mv_bouttonG.pack()
mv_bouttonH = Button(frame3, text="H", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_H)
mv_bouttonH.pack()
mv_bouttonB = Button(frame4, text="B", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_B)
mv_bouttonB.pack()

# ajout des frames
frame1.pack(side=RIGHT)
frame2.pack(side=LEFT)
frame3.pack(side=TOP)
frame4.pack(side=BOTTOM)

# afficher fenetre
fenetre.mainloop()
