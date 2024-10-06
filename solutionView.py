import sys
import tkinter as tk
import tkinter.font as tkFont


class App:

    def __init__(self, root, solution):
        """
        A class to display the solution
        Args:
            root: The root window
            solution: The solution as a string to be displayed
        """
        if solution == "" or solution == []:
            from tkinter import messagebox
            messagebox.showinfo("Error", "No solution found")
            sys.stderr = object
            root.destroy()
        print("solution view")
        root.title("Solution Viewer")
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width_percentage = 0.8
        height_percentage = 0.8
        width = int(screenwidth * width_percentage)
        height = int(screenheight * height_percentage)
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        alignstr = f'{width}x{height}+{x}+{y}'
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        title_font = tkFont.Font(family='Times', size=24, weight='bold')
        title_label = tk.Label(root, text="Solution", font=title_font, fg="#333333")
        title_label.place(relx=0.5, rely=0.05, anchor='n')
        solution_text = str(solution)
        print(solution_text)
        solution_font = tkFont.Font(family='Times', size=14)
        solution_display = tk.Label(root, text=solution_text, font=solution_font, fg="#333333", justify="center")
        solution_display.place(relx=0.5, rely=0.5, anchor='center')
        close_button = tk.Button(root, text="Close", command=root.destroy, font=title_font, fg="#000000", bg="#c0c0c0")
        close_button.place(relx=0.5, rely=0.9, anchor='s')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.update_idletasks()
    root.mainloop()
