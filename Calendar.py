# import calendar
import datetime as d
import tkinter
import tkcalendar


class Calendar:
    """Ici, on va tenter de recup la date actuelle pour pouvoir
     afficher le mois actuel et le suivant.
     Ensuite, on va tenter d'afficher le calendrier du mois actuel
     Puis de lier une tache avec une date.
     Il faudra egalement prevoir les evenements."""

print(d.datetime.today().strftime('%Y-%m-%d'))

root = tkinter.Tk()
cal = tkcalendar.Calendar(root)
cal.pack()
# calendar.prmonth(2023, 12)
root.mainloop()
