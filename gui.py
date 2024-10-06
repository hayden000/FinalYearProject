import tkinter as tk
import tkinter.font as tkFont

import Apps


class App:
    def __init__(self, root):
        """
        Constructor for the GUI.
        Args:
            root: The root of the GUI.
        Returns:
        """
        self.root = root
        root.title("Workflow Satisfiability Problem Solver")
        self.label_font = tkFont.Font(family='Times', size=18)
        root.geometry("800x600")
        root.resizable(width=True, height=True)
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.create_widgets(main_frame)

    def create_widgets(self, main_frame):
        """
        A function to create the widgets of the GUI.
        Args:
            main_frame: The main frame of the GUI.
        """
        tk.Label(main_frame, font=self.label_font, text="Workflow Satisfiability Problem Solver") \
            .grid(row=0, column=0, columnspan=2, pady=(0, 20))
        tk.Label(main_frame, font=self.label_font, text="Enter number of steps:") \
            .grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.steps_entry = tk.Entry(main_frame, font=self.label_font)
        self.steps_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        tk.Label(main_frame, font=self.label_font, text="Binding of duty:") \
            .grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.binding_entry = tk.Entry(main_frame, font=self.label_font)
        self.binding_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        tk.Label(main_frame, font=self.label_font, text="Separation of duty:") \
            .grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.separation_entry = tk.Entry(main_frame, font=self.label_font)
        self.separation_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        tk.Button(main_frame, bg="#c0c0c0", font=self.label_font, text="Enter Authorisations",
                  command=self.enter_authorisations_command) \
            .grid(row=4, column=0, columnspan=2, pady=20)
        for i in range(5):
            main_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            main_frame.grid_columnconfigure(i, weight=1)

    def parse_constraints(self, string, con):
        """
        A function to parse the constraints. And return a list of lists in the correct format.
        Args:
            string: The string to parse.
            con: The type of constraint.
        Returns:
            A list of lists in the correct format.
        """
        if string == "" or con == "":
            return []
        try:
            pairs = string.split(':')
            output = []
            if con.upper() == "SOD" or con.upper() == "BOD":
                for pair in pairs:
                    values = pair.split(',')
                    output.append([int(values[0]), int(values[1]), con.upper()])
            return output
        except ValueError:
            print("Error parsing constraints")
            return []

    def enter_authorisations_command(self):
        """
        Allows the user to enter the authorisations.
        """
        try:
            steps = int(self.steps_entry.get())
            bindings = str(self.binding_entry.get())
            separation = str(self.separation_entry.get())
            binding = self.parse_constraints(bindings, "BOD")
            separation = self.parse_constraints(separation, "SOD")
            rules = binding + separation
            self.root.withdraw()
            # window2 = tk.Toplevel(self.root)
            gui2 = Apps.authpage(self.root, steps,
                                 rules)
            # self.root.destroy()

        except ValueError:
            from tkinter import messagebox
            messagebox.showerror("Error", "Please enter valid entry")
            print("Please enter valid.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
