import tkinter as tk

MIDDLE_OF_SCREEN = "+700+300"
FONT = ("Helvetica", 12)


class WindowCreator:
    def __init__(self, root):
        self.root = root

        # Configure columns
        for i in range(2):  # Two columns
            self.root.grid_columnconfigure(i, weight=1)

        # Configure name, size of window and where it opens
        root.title("Kalender")
        root.geometry("500x500" + MIDDLE_OF_SCREEN)

        self.chk_value = tk.IntVar()

        self.top_frame()
        self.rvalue = tk.IntVar()
        week = self.create_frame(1, 0, "Woche")
        todo = self.create_frame(1, 1, "Neuen Aufgaben")

        # radiobutton
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        for i, day in enumerate(days):
            rbutton = tk.Radiobutton(week, text=day, variable=self.rvalue, value=i)
            rbutton.pack()

        # Buttons useless to remove
        input_text_to_do = tk.Label(todo, text="")
        input_text_to_do.pack()

        # Text Box
        self.text_enter = tk.StringVar()
        user_entry = tk.Entry(todo, bg="white", textvariable=self.text_enter)
        user_entry.pack()

        # Task Frame
        extra = self.create_frame(2, 0, "Zu Erledigen")
        extra2 = self.create_frame(2, 1, "Erledigt")

        # Button Task
        button_task = tk.Button(todo, text="Neue", command=lambda: self.create_task(extra))
        button_task.pack()

        # Button Save
        # button_save = tk.Button(todo, text="Speichern")
        # button_save.pack()

    def top_frame(self):
        top_frame = tk.Frame(self.root)
        top_frame.grid(row=0, column=0, columnspan=2)

        label = tk.Label(top_frame, text="Woche", font=FONT)
        label.pack(padx=10, pady=10)

    def create_frame(self, row, column, label_text):
        frame = tk.Frame(self.root, relief=tk.RIDGE, borderwidth=2)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label = tk.Label(frame, text=label_text, font=FONT)
        label.pack(expand=True, side=tk.TOP)

        return frame

    def launch(self, window):
        window.mainloop()

    def create_task(self, frame):
        """Create a task in the to do list
        Task has a name and a checkbox
        when checkbox crossed, task goes on the other frame"""

        texted = self.text_enter.get()
        valued = tk.IntVar()
        task = tk.Checkbutton(frame, text=texted, variable=valued)
        task.pack()

        return frame

# class tableauCalendrier:
# utiliser module calendrier



root = tk.Tk()
WindowCreator(root=root).launch(root)
