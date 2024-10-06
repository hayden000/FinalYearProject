import tkinter as tk

from Autharisations import App as AuthApp


# A driver function to open the tkinter screen
def authpage(root, steps, rules):
    open_authorizations(steps, rules)


def open_authorizations(steps, rules):
    auth_root = tk.Toplevel()
    AuthApp(auth_root, steps, rules)
