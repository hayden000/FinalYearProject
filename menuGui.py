import tkinter as tk
import tkinter.font as tkFont

import State
from gui import App as ConApp
from help import App as HelpApp


class App:

    def __init__(self, root):
        """
        Constructor for the menu GUI
        Args:
            root: The root of the GUI
        """
        # Creating buttons and labels
        self.root = root
        root.title("WSP Solver")
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width_percentage = 0.6
        height_percentage = 0.6
        width = int(screenwidth * width_percentage)
        height = int(screenheight * height_percentage)
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        alignstr = f'{width}x{height}+{x}+{y}'
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.selected_solver = tk.IntVar()
        main_frame = tk.Frame(root)
        main_frame.place(relx=0.5, rely=0.5, anchor='center')
        GLabel_768 = tk.Label(main_frame)
        ft = tkFont.Font(family='Times', size=38)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "WSP Solver"
        GLabel_768.grid(row=0, column=0, pady=20, columnspan=3)
        solver_frame = tk.Frame(main_frame)
        solver_frame.grid(row=1, column=0, columnspan=3)
        GRadio_124 = tk.Radiobutton(solver_frame, variable=self.selected_solver, value=1,
                                    command=self.GRadio_124_command)
        ft = tkFont.Font(family='Times', size=18)
        GRadio_124["font"] = ft
        GRadio_124["fg"] = "#333333"
        GRadio_124["justify"] = "center"
        GRadio_124["text"] = "SAT solver"
        GRadio_124.grid(row=0, column=0, padx=10)
        GRadio_154 = tk.Radiobutton(solver_frame, variable=self.selected_solver, value=2,
                                    command=self.GRadio_154_command)
        GRadio_154["font"] = ft
        GRadio_154["fg"] = "#333333"
        GRadio_154["justify"] = "center"
        GRadio_154["text"] = "Brute force"
        GRadio_154.grid(row=0, column=1, padx=10)
        GRadio_55 = tk.Radiobutton(solver_frame, variable=self.selected_solver, value=3, command=self.GRadio_55_command)
        GRadio_55["font"] = ft
        GRadio_55["fg"] = "#333333"
        GRadio_55["justify"] = "center"
        GRadio_55["text"] = "Pattern backtracking"
        GRadio_55.grid(row=0, column=2, padx=10)
        GLabel_601 = tk.Label(main_frame)
        ft = tkFont.Font(family='Times', size=20)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "center"
        GLabel_601["text"] = "Select a solver"
        GLabel_601.grid(row=2, column=0, pady=10, columnspan=3)
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=20)
        GButton_721 = tk.Button(button_frame, bg="#c0c0c0", command=self.GButton_721_command)
        ft = tkFont.Font(family='Times', size=18)
        GButton_721["font"] = ft
        GButton_721["fg"] = "#000000"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "Solve"
        GButton_721.grid(row=0, column=0, padx=20)
        GButton_287 = tk.Button(button_frame, bg="#c0c0c0", command=self.GButton_287_command)
        GButton_287["font"] = ft
        GButton_287["fg"] = "#000000"
        GButton_287["justify"] = "center"
        GButton_287["text"] = "Help"
        GButton_287.grid(row=0, column=1, padx=20)
        GButton_652 = tk.Button(button_frame, bg="#c0c0c0", command=self.GButton_652_command)
        GButton_652["font"] = ft
        GButton_652["fg"] = "#000000"
        GButton_652["justify"] = "center"
        GButton_652["text"] = "Exit"
        GButton_652.grid(row=0, column=2, padx=20)

    # Create radio buttons for the main menu
    def GRadio_124_command(self):
        print("Selected: SAT solver")

        State.solverType = "SAT"
        # State.setSolver("SAT")

    def GRadio_154_command(self):
        print("Selected: Brute force")

        State.solverType = "Brute"
        # State.setSolver("Brute")

    def GRadio_55_command(self):
        print("Selected: Bipartite matching")
        # state_instance = State()

        State.solverType = "PBT"
        # State.setSolver("PBT")

    # Open the next screen
    def GButton_721_command(self):
        try:
            if State.solverType != "PBT" or State.solverType != "Brute" or State.solverType != "SAT":
                self.root.withdraw()
                self.open_constraints()
        except:
            from tkinter import messagebox
            messagebox.showerror("Error", "Please select a solver")

    # Open the help screen
    def GButton_287_command(self):
        print("Help command")
        help_root = tk.Toplevel()
        help_app = HelpApp(help_root)

    # Exit the program button
    def GButton_652_command(self):
        self.root.destroy()

    def open_constraints(self):
        con_root = tk.Tk()
        ConApp(con_root)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.update_idletasks()
    root.mainloop()
