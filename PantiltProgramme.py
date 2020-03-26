from tkinter import *
import pantilthat

pantilthat.idle_timeout(0.5)

# definir les angles
def mvt_D():
	pantilthat.pan(-45)
	
def mvt_G():
	pantilthat.pan(45)
	
def mvt_H():
	pantilthat.tilt(-45)
	
def mvt_B():
	pantilthat.tilt(45)
	

# creation fenetre
window = Tk()

# personnalisation fenetre
window.title("Orientation camera")
window.geometry("480x360")
window.minsize(480, 360)
window.config(background='#41B77F')

# creation des frames
frame1 = Frame(window, bg='#41B77F')
frame2 = Frame(window, bg='#41B77F')
frame3 = Frame(window, bg='#41B77F')
frame4 = Frame(window, bg='#41B77F')

# ajout de boutons
mv_buttonD = Button(frame1, text="D", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_D)
mv_buttonD.pack()
mv_buttonG = Button(frame2, text="G", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_G)
mv_buttonG.pack()
mv_buttonH = Button(frame3, text="H", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_H)
mv_buttonH.pack()
mv_buttonB = Button(frame4, text="B", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_B)
mv_buttonB.pack()

# ajout des frames
frame1.pack(side=RIGHT)
frame2.pack(side=LEFT)
frame3.pack(side=TOP)
frame4.pack(side=BOTTOM)

# afficher fenetre
window.mainloop()
