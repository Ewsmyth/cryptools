# toast.py
import tkinter as tk

class Toast:
    def __init__(self, parent, message, duration=2500, kind="info"):
        # parent should be your root (tk.Tk)
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.top.overrideredirect(True)
        try:
            self.top.attributes("-topmost", True)
        except Exception:
            pass

        colors = {
            "info":    ("#0b5fa5", "#e8f4fd"),
            "success": ("#1b7a3f", "#e8f6ec"),
            "warning": ("#9a6b00", "#fff7e6"),
            "error":   ("#a12622", "#fdecea"),
        }
        fg, bg = colors.get(kind, colors["info"])

        lbl = tk.Label(self.top, text=message, bg=bg, fg=fg, padx=12, pady=8, bd=1, relief="solid")
        lbl.pack()

        # Defer placement until the root has a real size
        self.top.after(0, self._place_and_show)
        self.top.after(duration, self.top.destroy)

    def _place_and_show(self):
        self.parent.update_idletasks()
        # If parent is iconified or not mapped yet, try again shortly
        if not self.parent.winfo_ismapped():
            self.top.after(50, self._place_and_show)
            return

        pw = self.parent.winfo_width()
        ph = self.parent.winfo_height()
        px = self.parent.winfo_rootx()
        py = self.parent.winfo_rooty()

        tw = self.top.winfo_reqwidth()
        th = self.top.winfo_reqheight()

        x = px + max(0, pw - tw - 16)
        y = py + max(0, ph - th - 16)
        self.top.geometry(f"+{x}+{y}")

        # Bring to front for some window managers
        self.top.lift()
        try:
            self.top.focus_force()
        except Exception:
            pass
