from tkinter import *
import pantilthat

pantilthat.idle_timeout(0.5)

# definir les angles
def mvt_D3():
	pantilthat.pan(-40)
def mvt_D2():
	pantilthat.pan(-20)	
def mvt_D1():
	pantilthat.pan(-5)	
def mvt_G3():
	pantilthat.pan(40)	
def mvt_G2():
	pantilthat.pan(20)
def mvt_G1():
	pantilthat.pan(5)	
def mvt_H3():
	pantilthat.tilt(-40)	
def mvt_H2():
	pantilthat.tilt(-20)
def mvt_H1():
	pantilthat.tilt(-5)	
def mvt_B3():
	pantilthat.tilt(40)
def mvt_B2():
	pantilthat.tilt(20)
def mvt_B1():
	pantilthat.tilt(5)
	
# creation fenetre
fenetre = Tk()

# personnalisation fenetre
fenetre.title("Orientation camera")
fenetre.geometry("480x360")
fenetre.minsize(480, 360)
fenetre.config(background='#41B77F')


# ajout de boutons
mv_bouttonD3 = Button(fenetre, text="D3", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_D3)
mv_bouttonD3.place(x=410, y=155)
mv_bouttonD2 = Button(fenetre, text="D2", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_D2)
mv_bouttonD2.place(x=340, y=155)
mv_bouttonD1 = Button(fenetre, text="D1", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_D1)
mv_bouttonD1.place(x=270, y=155)
mv_bouttonG3 = Button(fenetre, text="G3", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_G3)
mv_bouttonG3.place(x=0, y=155)
mv_bouttonG2 = Button(fenetre, text="G2", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_G2)
mv_bouttonG2.place(x=70, y=155)
mv_bouttonG1 = Button(fenetre, text="G1", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_G1)
mv_bouttonG1.place(x=140, y=155)
mv_bouttonH3 = Button(fenetre, text="H3", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_H3)
mv_bouttonH3.place(x=205, y=0)
mv_bouttonH2 = Button(fenetre, text="H2", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_H2)
mv_bouttonH2.place(x=205, y=50)
mv_bouttonH1 = Button(fenetre, text="H1", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_H1)
mv_bouttonH1.place(x=205, y=100)
mv_bouttonB3 = Button(fenetre, text="B3", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_B3)
mv_bouttonB3.place(x=205, y=310)
mv_bouttonB2 = Button(fenetre, text="B2", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_B2)
mv_bouttonB2.place(x=205, y=260)
mv_bouttonB1 = Button(fenetre, text="B1", font=("Courrier", 25), bg='white', fg='#41B77F', command=mvt_B1)
mv_bouttonB1.place(x=205, y=210)

# afficher fenetre
fenetre.mainloop()
