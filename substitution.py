import tkinter as tk

class SubstitutionView(tk.Frame):
    """
    Simple demo UI for a monoalphabetic substitution view.
    Replace with your actual logic/key handling.
    """
    def __init__(self, parent, show_toast=None):
        super().__init__(parent, bg="white", bd=1, relief=tk.SOLID)
        self.show_toast = show_toast or (lambda *a, **k: None) 

        # Grid config
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = tk.Label(self, text="Substitution Cipher", font=("Segoe UI", 16, "bold"), bg="white")
        title.grid(row=0, column=0, sticky="w", padx=12, pady=(12, 6))

        key_row = tk.Frame(self, bg="white")
        key_row.grid(row=1, column=0, sticky="ew", padx=12)
        key_row.grid_columnconfigure(1, weight=1)

        tk.Label(key_row, text="Key (26 letters):", bg="white").grid(row=0, column=0, sticky="w", padx=(0,8), pady=6)
        self.key_entry = tk.Entry(key_row)
        self.key_entry.grid(row=0, column=1, sticky="ew", pady=6)
        self.key_entry.insert(0, "ZYXWVUTSRQPONMLKJIHGFEDCBA")  # example key

        self.input_text = tk.Text(self, height=6)
        self.input_text.grid(row=2, column=0, sticky="nsew", padx=12, pady=6)

        btns = tk.Frame(self, bg="white")
        btns.grid(row=3, column=0, sticky="ew", padx=12)
        btns.grid_columnconfigure(0, weight=1)
        btns.grid_columnconfigure(1, weight=1)

        tk.Button(btns, text="Encrypt", command=self.encrypt).grid(row=0, column=0, sticky="ew", pady=(6, 12), padx=(0,6))
        tk.Button(btns, text="Decrypt", command=self.decrypt).grid(row=0, column=1, sticky="ew", pady=(6, 12), padx=(6,0))

        self.output = tk.Text(self, height=6, state="disabled")
        self.output.grid(row=4, column=0, sticky="nsew", padx=12, pady=(0, 12))

    def _build_maps(self, key):
        key = key.strip()
        if len(key) != 26 or not key.isalpha():
            raise ValueError("Key must be 26 alphabetic characters.")
        key_up = key.upper()
        plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        enc_map = {plain[i]: key_up[i] for i in range(26)}
        dec_map = {v: k for k, v in enc_map.items()}
        # Also support lowercase
        enc_map.update({k.lower(): v.lower() for k, v in enc_map.items()})
        dec_map.update({k.lower(): v.lower() for k, v in dec_map.items()})
        return enc_map, dec_map

    def encrypt(self):
        try:
            enc_map, _ = self._build_maps(self.key_entry.get())
        except ValueError as e:
            self._show_error(str(e))
            return
        text = self.input_text.get("1.0", "end-1c")
        result = "".join(enc_map.get(ch, ch) for ch in text)
        self._set_output(result)

    def decrypt(self):
        try:
            _, dec_map = self._build_maps(self.key_entry.get())
        except ValueError as e:
            self._show_error(str(e))
            return
        text = self.input_text.get("1.0", "end-1c")
        result = "".join(dec_map.get(ch, ch) for ch in text)
        self._set_output(result)

    def _set_output(self, text):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.config(state="disabled")

    def _show_error(self, msg):
        # Minimal inline error display; replace with dialogs if you prefer
        self._set_output(f"[Error] {msg}")
