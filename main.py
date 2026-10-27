import tkinter as tk
from bmi_gui import BmiApplication
import bmi_func as core

if __name__ == "__main__":
    core.init_storage()
    root = tk.Tk()
    app = BmiApplication(master=root)
    root.mainloop()
