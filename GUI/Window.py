"""Ce fichier contient la classe Window qui permet de générer la fenêtre et gérer son comportement
    D'autrepart, on essaye de faire un truc joli donc on utilise custom Tkinter !!!"""

import tkinter as tk
import GUI.Frames as Fr

TITLE = "Star-lendar"
FONT = ("Helvetica", 12)

# How to get native the middle of the screen?
MIDDLE_OF_SCREEN_LAPTOP = "+400+100"
MIDDLE_OF_SCREEN = "+700+300"


class WindowCreator(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # base_frame = tk.Frame(self)

        self.title("TEST")
        self.geometry("500x500" + MIDDLE_OF_SCREEN)

        self.choice_frame = Fr.ChoiceOfForceSide(self)
        #self.choice_frame.pack(anchor="nw")
        self.newest = Fr.MainManagementFrame(self)

        #### MEGATEST ###
        self.confirm_button = tk.Button(self, text="Confirm", command=lambda: self.destroyer(self.choice_frame))
        self.confirm_button.pack()

        est1 = Fr.MainManagementFrame.create_frame(self.newest,0,0, "bonjour")
        est1.grid()

    def destroyer(self, frame):
        frame.pack_forget()
        self.newest.pack()
        self.confirm_button.pack_forget()


root = WindowCreator()
root.mainloop()
