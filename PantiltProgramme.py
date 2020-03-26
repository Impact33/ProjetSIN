from tkinter import *

# creation fenetre
window = Tk()

# personnalisation fenetre
window.title("Orientation camera")
window.geometry("480x360")
window.minsize(480, 360)
window.config(background='#41B77F')

# creation de la frame
frame = Frame(window, bg='#41B77F')

# ajout de boutons
mv_button = Button(frame, text="Droite", font=("Courrier", 25), bg='white', fg='#41B77F')
mv_button.pack()

# ajout de la frame
frame.pack(expand=YES)

# afficher fenetre
window.mainloop()
