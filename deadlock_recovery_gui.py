import customtkinter as ctk
from tkinter import scrolledtext
import psutil
from deadlock_recovery import resolve_deadlock, terminate_process
from deadlock_detection import detect_deadlocks


class DeadlockRecoveryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Deadlock Recovery")
        self.geometry("900x600")
        ctk.set_appearance_mode("light")

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="green", height=50)
        self.header_frame.pack(fill="x")
        self.header_label = ctk.CTkLabel(self.header_frame, text="Deadlock Recovery", font=("Arial", 18, "bold"),
                                         text_color="white")
        self.header_label.pack(side="left", padx=10)
        self.appearance_mode = ctk.CTkOptionMenu(self.header_frame, values=["Light", "Dark"], command=self.change_theme)
        self.appearance_mode.pack(side="right", padx=10, pady=10)

        # Main layout
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Action Panel (Left Panel)
        self.action_frame = ctk.CTkFrame(self.main_frame, width=300)
        self.action_frame.pack(side="right", padx=20, pady=20, fill="y")

        self.resolve_button = ctk.CTkButton(self.action_frame, text="Detect & Resolve Deadlocks",
                                            command=self.run_deadlock_resolution)
        self.resolve_button.pack(pady=10,padx=10, fill="x")

        # Output Box (Right Panel)
        self.output_frame = ctk.CTkFrame(self.main_frame)
        self.output_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap="word", height=15)
        self.output_text.pack(expand=True, fill="both", padx=10, pady=10)

    def run_deadlock_resolution(self):
        deadlocks = detect_deadlocks()  # Detect actual deadlocks
        output = resolve_deadlock(deadlocks)  # Resolve if found
        self.output_text.insert("end", output + "\n")
        self.output_text.see("end")

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = DeadlockRecoveryApp()
    app.mainloop()
