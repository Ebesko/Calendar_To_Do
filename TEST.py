import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 200))

        # Create a vertical box sizer for the main frame
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a static text row for the days of the week
        days_of_week_row = wx.StaticText(self, label="Sun Mon Tue Wed Thu Fri Sat")
        main_sizer.Add(days_of_week_row, 0, wx.ALL | wx.EXPAND, border=10)

        # Create a grid sizer for the calendar (2 rows, 7 columns)
        calendar_grid = wx.GridSizer(2, 7, 0, 0)

        # Add date labels to the grid (you can customize this part)
        for day in range(1, 8):
            label = wx.StaticText(self, label=str(day))
            calendar_grid.Add(label, 0, wx.ALL | wx.EXPAND, border=5)

        for date in range(8, 15):
            label = wx.StaticText(self, label=str(date))
            calendar_grid.Add(label, 0, wx.ALL | wx.EXPAND, border=5)

        # Add the grid sizer to the main sizer
        main_sizer.Add(calendar_grid, 0, wx.ALL | wx.EXPAND, border=10)

        # Set the main sizer for the frame
        self.SetSizer(main_sizer)

        self.Show()


app = wx.App()
frame = MyFrame(None, "Simple Week Display")
app.MainLoop()
