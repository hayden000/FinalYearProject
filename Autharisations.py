import tkinter as tk
import tkinter.font as tkFont

import Logic
import State
import add
import ortool
from solutionView import App as SolutionViewApp


class App:
    def __init__(self, root, num_steps, rules):
        """
        A class for the authorisations GUI
        Args:
            root: The root of the GUI
            num_steps int: The number of steps in the workflow
            rules: The bod and sod rules in the workflow

        """
        self.root = root
        root.title("Workflow Satisfiability Problem Solver")
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        self.width, self.height = 800, 600
        x = (screenwidth - self.width) / 2
        y = (screenheight - self.height) / 2
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, x, y)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        title_font = tkFont.Font(family='Times', size=24, weight='bold')
        label_font = tkFont.Font(family='Times', size=18)
        label = tk.Label(root, font=title_font, fg="#333333", justify="center", text="Authorisations")
        label.place(x=self.width // 2 - 100, y=20, width=200, height=50)
        self.entry_boxes = self.create_entry_boxes(root, num_steps, label_font)
        compute_button = tk.Button(root, bg="#c0c0c0", font=label_font, text="Compute",
                                   command=lambda: self.compute_command(rules))
        compute_button.place(x=self.width // 2 - 60, y=self.height - 60, width=120, height=40)

    def create_entry_boxes(self, root, num_steps, label_font):
        """
        Places the entry boxes for the authorisations in the GUI
        Args:
            root: The root of the GUI
            num_steps int: The number of steps in the workflow as this is the number of entry boxes required on the GUI
            label_font: The font of the labels
        """
        entry_boxes = []
        for step in range(1, num_steps + 1):
            label_text = f"Step {step}:"
            entry = tk.Entry(root, borderwidth="1px", font=label_font, fg="#333333", justify="center")
            entry.place(x=self.width // 4, y=(step * self.height) // (num_steps + 1), width=400, height=35)
            label = tk.Label(root, font=label_font, fg="#333333", justify="center", text=label_text)
            label.place(x=self.width // 4 - 50, y=(step * self.height) // (num_steps + 1), width=70, height=35)
            entry_boxes.append(entry)
        return entry_boxes

    def parse_list(self, authlst):
        """
        Gets the list of autharisations into the correct format for the solver
        Args:
            authlst: The list of authorisations

        Returns:
        The parsed list of authorisations
        """
        print('authlist ', authlst)
        try:
            parsed_list = []
            for item in authlst:
                if item != "":
                    step = []
                    for num in item.split(','):
                        step.append(int(num))
                    parsed_list.append(step)
                else:
                    parsed_list.append([])
            return parsed_list
        except ValueError:
            print("Error")
            return []

    def compute_command(self, rules):
        """
        A button command to compute the solution, passes the rules to the solver based on the solver type selected in the GUI
        Args:
            rules: The bod and sod rules in the workflow
        """
        auths = self.get_auths()
        print("auths:", auths)
        print("rules: ", rules)
        solution = []
        solveType = State.solverType
        if solveType == "Brute":
            solution = Logic.main(rules, auths)
        elif solveType == "SAT":
            solution = ortool.SATsolver(rules, auths)
        elif solveType == "PBT":
            solution = add.pbtSolve(rules, auths)
        solution_view_app = SolutionViewApp(tk.Toplevel(), solution)
        self.root.destroy()

    def get_auths(self):
        """
        Returns the authorisations from the GUI

        Returns:
        The parsed authorisations
        """
        auths = []
        for entry in self.entry_boxes:
            auths.append(entry.get())
        return self.parse_list(auths)
