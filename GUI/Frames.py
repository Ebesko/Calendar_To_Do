"""Ce fichier contient la classe Frame qui permet la gestion des sections"""
import tkinter
import tkinter as tk
from tkinter import ttk

FONT = ("Helvetica", 12)


class ChoiceOfForceSide(tk.Frame):
    """This class allows the user to choose between Jedi and Sith"""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Choose a side of the force, you must.", font=FONT)
        label.pack(anchor="nw")

        BRUH = tk.PhotoImage(file="Jedi.gif")
        lalala = tk.Label(self, image=BRUH)
        lalala.pack()

        self.radio_value = tk.IntVar()

        self.choice(MainManagementFrame(parent))

    def choice(self, frame):
        # Jedi
        jedi_button = tk.Radiobutton(self, text="Jedi", variable=self.radio_value, value=1)
        jedi_button.pack(side="left", padx=10, pady=5, anchor="w")

        # Sith
        sith_button = tk.Radiobutton(self, text="Sith", variable=self.radio_value, value=2)
        sith_button.pack(side="right", padx=10, pady=5, anchor="w")


class MainManagementFrame(tk.Frame):
    """this frame is the basis of the app. It manages the tasks and everything."""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MEGA-TEST.", font=FONT)
        label.pack(anchor="nw")

    def create_frame(self, row, column, label_text):
        frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label = tk.Label(frame, text=label_text, font=("Helvetica", 12))
        label.pack(side=tk.TOP)

        return frame


