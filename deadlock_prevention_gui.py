import customtkinter as ctk
from tkinter import scrolledtext
import ast
from deadlock_prevention import is_safe_state
class DeadlockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Deadlock Prevention")
        self.geometry("900x600")
        ctk.set_appearance_mode("light")

        # Default values
        self.default_available = [3, 3, 2]
        self.default_max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
        self.default_allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="green", height=50,corner_radius=0)
        self.header_frame.pack(fill="x")
        self.header_label = ctk.CTkLabel(self.header_frame, text="Deadlock Prevention", font=("Arial", 18, "bold"),
                                         text_color="white")
        self.header_label.pack(side="left", padx=10)
        self.appearance_mode = ctk.CTkOptionMenu(self.header_frame, values=["Light", "Dark"], command=self.change_theme)
        self.appearance_mode.pack(side="right", padx=10, pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=30, pady=30, fill="both", expand=True)


        self.input_frame = ctk.CTkFrame(self.main_frame,width=300,height=300)
        self.input_frame.pack(side="right", padx=20, pady=20, fill="y")

        self.available_entry = ctk.CTkEntry(self.input_frame, placeholder_text=str(self.default_available))
        self.available_entry.pack(padx=10,pady=5, fill="x")

        self.max_demand_entry = ctk.CTkEntry(self.input_frame, placeholder_text=str(self.default_max_demand))
        self.max_demand_entry.pack(padx=10,pady=5, fill="x")

        self.allocation_entry = ctk.CTkEntry(self.input_frame, placeholder_text=str(self.default_allocation))
        self.allocation_entry.pack(padx=10,pady=5, fill="x")

        self.check_button = ctk.CTkButton(self.input_frame, text="Check Deadlocks", command=self.run_deadlock_check)
        self.check_button.pack(pady=10,padx=10, fill="x")

        # Output Box (Right Panel)
        self.output_frame = ctk.CTkFrame(self.main_frame)
        self.output_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap="word", height=15)
        self.output_text.pack(expand=True, fill="both", padx=10, pady=10)

    def run_deadlock_check(self):
        try:
            available = ast.literal_eval(
                self.available_entry.get()) if self.available_entry.get() else self.default_available
            max_demand = ast.literal_eval(
                self.max_demand_entry.get()) if self.max_demand_entry.get() else self.default_max_demand
            allocation = ast.literal_eval(
                self.allocation_entry.get()) if self.allocation_entry.get() else self.default_allocation
        except Exception as e:
            self.output_text.insert("end", f"\nInvalid input format! Error: {e}\n")
            return

        safe, sequence = is_safe_state(available, max_demand, allocation)

        output = f"\n✅ System is in a Safe State. Safe Sequence: {sequence}\n" if safe else "\nDeadlock Risk! System is in an Unsafe State.\n"

        with open("deadlock_prevention_output.txt", "w",encoding="utf8") as file:
            file.write(output)

        self.output_text.insert("end", output)
        self.output_text.see("end")

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = DeadlockApp()
    app.mainloop()