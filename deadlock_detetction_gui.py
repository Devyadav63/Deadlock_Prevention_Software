import customtkinter as ctk
from tkinter import scrolledtext
from deadlock_detection import detect_resource_contention
from networkx.algorithms.bipartite.basic import color

# Initialize CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class DeadlockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Deadlock Detection")
        self.geometry("800x500")

        # Configure Grid Layout
        self.grid_rowconfigure(1, weight=2)  # Main interactive area
        self.grid_rowconfigure(2, weight=4)  # Scrollable output area
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        # Header Frame
        self.header_frame = ctk.CTkFrame(self, height=50, corner_radius=0, fg_color="blue")
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.header_label = ctk.CTkLabel(self.header_frame, text="  Deadlock Detection", font=("Arial", 18, "bold"),text_color="white")
        self.header_label.pack(side="left", padx=10)

        # Theme Switch
        self.appearance_mode = ctk.CTkOptionMenu(self.header_frame, values=["Light", "Dark"],
                                                 command=self.change_theme)
        self.appearance_mode.pack(side="right", padx=10, pady=10)

        # Main Interactive Area
        self.main_button = ctk.CTkButton(self, text="Check Deadlocks", font=("Arial", 18, "bold"),
                                         height=100, command=self.run_deadlock_check)
        self.main_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        # Scrollable Output Frame
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap="word", height=10)
        self.output_text.pack(expand=True, fill="both", padx=10, pady=10)

        # Buttons on Side Panel
        # Configure Side Panel
        self.side_panel = ctk.CTkFrame(self)
        self.side_panel.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        # Configure row weight so buttons take half of the side panel
        self.side_panel.grid_rowconfigure(0, weight=1)
        self.side_panel.grid_rowconfigure(1, weight=1)
        self.side_panel.grid_columnconfigure(0, weight=1)  # Ensure buttons expand properly

        # Buttons inside Side Panel (each taking half the height)
        self.check_again_btn = ctk.CTkButton(self.side_panel, text="Check Again", command=self.run_deadlock_check,
                                             height=80,fg_color="blue")
        self.check_again_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.main_menu_btn = ctk.CTkButton(self.side_panel, text="Main Menu", command=self.clear_output, height=80)
        self.main_menu_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def run_deadlock_check(self):
        """Simulate deadlock detection output."""
        detect_resource_contention()
        with open("deadlock_prevention_output.txt", "r", encoding="utf-8") as file:
            output_text = file.read()
        file.close()
        self.output_text.insert("end", output_text)
        self.output_text.see("end")

    def clear_output(self):
        """Clears the output text box."""
        self.output_text.delete("1.0", "end")

    def change_theme(self, theme):
        """Switch between light and dark mode."""
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = DeadlockApp()
    app.mainloop()
