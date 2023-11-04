import tkinter as tk

MIDDLE_OF_SCREEN = "+700+300"
FONT = ("Helvetica", 12)


class WindowCreator:
    def __init__(self, root):
        self.root = root

        # Configure name, size of window and where it opens
        root.title("Kalender")
        root.geometry("500x500" + MIDDLE_OF_SCREEN)
        self.top_frame()

        # Configure columns
        for i in range(2):  # Two columns
            self.root.grid_columnconfigure(i, weight=1)

        # Variables of input widgets
        #self.rvalue = tk.IntVar()
        self.text_enter = tk.StringVar()
        self.radio_value = tk.IntVar()

        # Main frames
        week = self.create_frame(1, 0, "Woche")
        todo = self.create_frame(1, 1, "Verwaltung")
        # Task Frames
        extra = self.create_frame(2, 0, "Zu Erledigen")
        extra2 = self.create_frame(2, 1, "Erledigt")
        # Fill the Todo frame
        self.create_management(todo, extra, extra2)

        # listbox of days
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        self.days_scroll = self.create_scrolllist(frame=week, listed=days)

        # List of Tasks (TEST)
        self.task_list = []

    def create_scrolllist(self, frame, listed):
        # Create a Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Listbox and link it to the Scrollbar
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        listbox.pack(fill=tk.BOTH, expand=False)
        scrollbar.config(command=listbox.yview)

        # Add items to the Listbox
        for item in listed:
            listbox.insert(tk.END, item)

        return listbox

    def create_management(self, frame, other, finish):
        """Create the management system for task:
        You can create a task with a name,
        a day of doing, and a theme : info or maths"""
        # Text input for the name of the task
        entry_named = tk.Label(frame, text="Aufgabename: ", font=FONT)
        entry_named.pack()
        user_entry = tk.Entry(frame, bg="white", textvariable=self.text_enter)
        user_entry.pack()

        # Radiobutton for Mathe oder Info
        themes = ["Informatik", "Mathe"]
        for i, item in enumerate(themes):
            theme_choice = tk.Radiobutton(frame, text=item, variable=self.radio_value, value=i)
            theme_choice.pack()

        # Task Button
        button_task = tk.Button(frame, text="Neue Aufgabe", command=lambda: self.create_task(other, finish))
        button_task.pack()

    def saving_button(self, frame):
        # Button Save
        button_save = tk.Button(frame, text="Speichern")
        button_save.pack()

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

    def create_task(self, frame, frame2):
        """Create a task in the to do list
        Task has a name and a checkbox
        when checkbox crossed, task goes on the other frame"""

        texted = self.text_enter.get()
        valued = tk.IntVar()
        day_selected = str((self.days_scroll.get(self.days_scroll.curselection())))

        if self.radio_value.get() == 0:
            themed = "Informatik: "
        else :
            themed = "Mathe: "
        task_name = themed + texted + " Before: " + day_selected

        def on_checkbox_checked():
            list_checked = []
            if valued.get() == 1:
                task.pack_forget()  # Remove the task from the current frame
                task2 = tk.Checkbutton(frame2, text=task_name, variable=valued, command=lambda: on_checkbox_checked())
                task2.pack()
                list_checked.append(task2)
                print(list_checked)

        task = tk.Checkbutton(frame, text=task_name, variable=valued, command=lambda: on_checkbox_checked())
        task.pack()

    def task_status(self, task_value):
        if task_value.get() == 1:
            print("TRUE")
        else:
            print("FALSE")
        #self.task_status(task.get())

    def launch(self, window):
        window.mainloop()

# class tableauCalendrier:
# utiliser module calendrier

root = tk.Tk()
WindowCreator(root=root).launch(root)
