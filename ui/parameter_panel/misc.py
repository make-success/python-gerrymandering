import tkinter as tk


class HoverInfo:
    """Shows text when mouse is hovered on given widget"""

    def __init__(self, widget, text, width=180):
        self.width = width
        self.widget, self.text = widget, text
        self.widget.bind('<Enter>', self.showtip)
        self.widget.bind('<Leave>', self.hidetip)
        self.top_level = None

    def showtip(self, _):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.top_level = tk.Toplevel(self.widget)
        self.top_level.wm_overrideredirect(True)  # leaves only the label and removes the app window
        self.top_level.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.top_level, text=self.text, justify='left', background="#ffffff", relief='solid',
                         borderwidth=1, wraplength=self.width)
        label.pack(ipadx=1)

    def hidetip(self, _=None):
        if self.top_level:
            self.top_level.destroy()
        self.top_level = None

    def delete(self):
        self.hidetip()
        self.widget.unbind('<Enter>')
        self.widget.unbind('<Leave>')


class InvalidParameter:
    def __init__(self, message):
        self.message = message