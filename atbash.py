import tkinter as tk
from tkinter import ttk
import string

class AtbashView(tk.Frame):
    """
    Simple demo UI for the ATBASH view.
    Replace the widgets/logic here with your actual ATBASH tool.
    """
    def __init__(self, parent, show_toast=None):
        super().__init__(parent, bg="white", bd=1, relief=tk.SOLID)
        self.show_toast = show_toast or (lambda *a, **k: None)

        title = tk.Label(self, text="ATBASH Cipher", font=("Segoe UI", 16, "bold"), bg="white")
        title.grid(row=0, column=0, columnspan=3, sticky="w", padx=0, pady=(12, 6))

        self.input_text = tk.Text(self, height=6)
        self.input_text.grid(row=1, rowspan=2, column=0, columnspan=9, sticky="nsew", padx=12, pady=6)

        spaces_label = tk.Label(self, text="Spaces:", font=("Segoe UI", 10, "bold"), bg="white")
        spaces_label.grid(row=3, column=0, sticky="nsew", padx=0, pady=(0, 0))

        options = [-1, 0, 5, 10]

        self.dropdown_box = ttk.Combobox(self, values=options)
        self.dropdown_box.current(0)
        self.dropdown_box.grid(row=3, column=1, columnspan=2)

        run_btn = tk.Button(self, text="Encode / Decode", command=self.run_atbash)
        run_btn.grid(row=4, column=1, columnspan=3, sticky="ew", padx=12, pady=(6, 12))

        self.output = tk.Text(self, height=6, state="disabled")
        self.output.grid(row=5, rowspan=2, column=0, columnspan=9, sticky="nsew", padx=12, pady=(0, 12))
        self.grid_rowconfigure(4, weight=1)

    def run_atbash(self):
        text = self.input_text.get("1.0", "end-1c").upper()

        # Convert combobox -> int safely
        try:
            selected_space = int(self.dropdown_box.get())
        except ValueError:
            if self.show_toast:
                self.show_toast("Spaces must be an integer.", kind="error")
            return

        # Atbash first so grouping applies to ciphertext
        upper_alpha = string.ascii_uppercase
        reverse = upper_alpha[::-1]
        trans = str.maketrans(upper_alpha, reverse)
        cipher = text.translate(trans)

        # Apply spacing options
        if selected_space == -1:
            spaced = cipher
        elif selected_space == 0:
            spaced = cipher.replace(" ", "")
        elif selected_space >= 1:
            compact = cipher.replace(" ", "")
            spaced = " ".join(compact[i:i+selected_space] for i in range(0, len(compact), selected_space))
        else:
            if self.show_toast:
                self.show_toast("Invalid spaces option.", kind="warning")
            return

        self._write_output(spaced)
        if self.show_toast:
            self.show_toast("Encoded with Atbash.", kind="success", duration=1800)

    def _write_output(self, text):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.config(state="disabled")
