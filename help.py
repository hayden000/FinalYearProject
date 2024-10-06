import tkinter as tk
import tkinter.font as tkFont
from tkinter import Scrollbar, Text, Button


class App:
    def __init__(self, root):
        """
        A class to display the help screen.
        Args:
            root: The root window.
        """
        root.title("Help")
        width = 800
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        title_font = tkFont.Font(family='Times', size=20, weight='bold')
        GLabel_388 = tk.Label(root)
        GLabel_388["font"] = title_font
        GLabel_388["fg"] = "#333333"
        GLabel_388["justify"] = "center"
        GLabel_388["text"] = "Help"
        GLabel_388.place(x=300, y=40, width=200, height=40)
        help_text = "To use the solver select the solver type and then proceed to enter the bod and sod constraints. Then enter the number of users and step in the solver instance. Proceed to the next screen and enter the constraints for each step. Then pressing the compute button will display the resulting solution. "
        help_font = tkFont.Font(family='Times', size=14)
        text_widget = Text(root, wrap="word", font=help_font)
        text_widget.insert("1.0", help_text)
        text_widget.place(x=50, y=100, width=700, height=400)
        scrollbar = Scrollbar(root, command=text_widget.yview)
        scrollbar.place(x=750, y=100, height=400)
        text_widget.config(yscrollcommand=scrollbar.set)
        close_button = Button(root, text="Close", command=root.destroy)
        close_button.place(x=350, y=520, width=100, height=30)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
