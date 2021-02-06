import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("300x200") 

        frame = tk.Frame(self.master, width = 120, bg = 'blue')
        frame.pack(side = tk.RIGHT, fill = tk.Y)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
