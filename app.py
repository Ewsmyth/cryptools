import tkinter as tk
from tkinter import messagebox
from atbash import AtbashView
from substitution import SubstitutionView
from toast import Toast

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CrypTools")
        self.geometry("800x500")

        # ===== Top native menubar =====
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menubar)

        # ===== Root grid config =====
        # Row 0: second bar (ATBASH/Substitution)
        # Row 1: main content
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ===== Faux menubar (second row) =====
        self.second_bar = tk.Frame(self, bd=1, relief=tk.RAISED)
        self.second_bar.grid(row=0, column=0, sticky="ew")
        self.second_bar.grid_columnconfigure(0, weight=0)
        self.second_bar.grid_columnconfigure(1, weight=0)
        self.second_bar.grid_columnconfigure(2, weight=1)  # spacer

        # ATBASH tab
        self.atbash_mb = tk.Menubutton(self.second_bar, text="ATBASH", relief=tk.FLAT, padx=12, pady=6)
        atbash_menu = tk.Menu(self.atbash_mb, tearoff=0)
        self.atbash_mb.config(menu=atbash_menu)
        self.atbash_mb.grid(row=0, column=0, sticky="w")
        self.atbash_mb.bind("<Button-1>", lambda e: self.switch_view("atbash"))  # left-click acts like selecting the tab

        # Substitution tab
        self.sub_mb = tk.Menubutton(self.second_bar, text="Substitution", relief=tk.FLAT, padx=12, pady=6)
        sub_menu = tk.Menu(self.sub_mb, tearoff=0)
        self.sub_mb.config(menu=sub_menu)
        self.sub_mb.grid(row=0, column=1, sticky="w")
        self.sub_mb.bind("<Button-1>", lambda e: self.switch_view("substitution"))

        # Optional hover effect
        #def on_enter(e): e.widget.config(relief=tk.GROOVE)
        #def on_leave(e): e.widget.config(relief=tk.FLAT)
        #for mb in (self.atbash_mb, self.sub_mb):
        #    mb.bind("<Enter>", on_enter)
        #    mb.bind("<Leave>", on_leave)

        # ===== Main content area =====
        self.content = tk.Frame(self, bg="#f4f4f4")
        self.content.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self._current_view = None  # holds the active Frame
        self.switch_view("atbash")  # default opened tab

    def show_toast(self, message, kind="info", duration=2500):
        Toast(self, message, duration=duration, kind=kind)

    # -------- File menu actions --------
    def save_file(self):
        messagebox.showinfo("Save", "Save option selected (implement your save logic).")

    def exit_app(self):
        self.quit()

    # -------- View switching --------
    def switch_view(self, name: str):
        # Destroy previous view if present
        if self._current_view is not None and self._current_view.winfo_exists():
            self._current_view.destroy()

        # Instantiate the requested view from its module/class
        if name.lower() == "atbash":
            self._current_view = AtbashView(self.content, show_toast=self.show_toast)
            # faux “selected” look
            self.atbash_mb.config(relief=tk.GROOVE)
            self.sub_mb.config(relief=tk.FLAT)
        elif name.lower() == "substitution":
            self._current_view = SubstitutionView(self.content, show_toast=self.show_toast)
            self.atbash_mb.config(relief=tk.FLAT)
            self.sub_mb.config(relief=tk.GROOVE)
        else:
            raise ValueError(f"Unknown view: {name}")

        # Place the view
        self._current_view.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    App().mainloop()
