import customtkinter as ctk
from tkinter import scrolledtext, StringVar
import psutil
from system_monitor import get_system_processes
from deadlock_detection import detect_resource_contention
import ast
from deadlock_prevention import is_safe_state
from deadlock_recovery import resolve_deadlock, terminate_process
from deadlock_detection import detect_deadlocks
class ProcessMonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("System Process Monitor")
        self.geometry("900x600")
        ctk.set_appearance_mode("light")

        # Default values for Banker's Algorithm
        self.default_available = [3, 3, 2]
        self.default_max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
        self.default_allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="green", height=50,corner_radius=0)
        self.header_frame.pack(fill="x")
        self.header_label = ctk.CTkLabel(self.header_frame, text="Deadlock Recovery and Prevention System", font=("Arial", 18, "bold"),
                                         text_color="white")
        self.header_label.pack(side="left", padx=10)
        self.appearance_mode = ctk.CTkOptionMenu(self.header_frame, values=["Light", "Dark"], command=self.change_theme)
        self.appearance_mode.pack(side="right", padx=10, pady=10)

        # Main layout
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Action Panel (Right Panel)
        self.action_frame = ctk.CTkFrame(self.main_frame, width=300)
        self.action_frame.pack(side="right", padx=20, pady=20, fill="y")

        self.refresh_button = ctk.CTkButton(self.action_frame, text="Refresh Process List",
                                            command=self.display_process_info)
        self.refresh_button.pack(pady=10,padx=10, fill="x")

        self.detect_deadlock_button = ctk.CTkButton(self.action_frame, text="Detect Deadlocks",
                                                    command=self.detect_deadlock)
        self.detect_deadlock_button.pack(pady=10,padx=10, fill="x")

        # Resource Values Adjustment
        self.resource_label = ctk.CTkLabel(self.action_frame, text="Modify Available Resources:")
        self.resource_label.pack(pady=5)

        self.available_var = StringVar(value=str(self.default_available))
        self.available_entry = ctk.CTkEntry(self.action_frame, textvariable=self.available_var)
        self.available_entry.pack(pady=5,padx=10, fill="x")

        self.max_demand_var = StringVar(value=str(self.default_max_demand))
        self.max_demand_entry = ctk.CTkEntry(self.action_frame, textvariable=self.max_demand_var)
        self.max_demand_entry.pack(pady=5, padx=10,fill="x")

        self.allocation_var = StringVar(value=str(self.default_allocation))
        self.allocation_entry = ctk.CTkEntry(self.action_frame, textvariable=self.allocation_var)
        self.allocation_entry.pack(pady=5,padx=10, fill="x")

        self.apply_resources_button = ctk.CTkButton(self.action_frame, text="Apply Resource Changes",
                                                    command=self.apply_resources)
        self.apply_resources_button.pack(pady=10,padx=10, fill="x")

        self.check_safety_button = ctk.CTkButton(self.action_frame, text="Check System Safety",
                                                 command=self.check_system_safety)
        self.check_safety_button.pack(pady=10, padx=10,fill="x")

        self.resolve_deadlock_button = ctk.CTkButton(self.action_frame, text="Resolve Deadlocks",
                                                     command=self.resolve_deadlock)
        self.resolve_deadlock_button.pack(pady=10,padx=10, fill="x")

        # Output Box (Right Panel)
        self.output_frame = ctk.CTkFrame(self.main_frame)
        self.output_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap="word", height=15)
        self.output_text.pack(expand=True, fill="both", padx=10, pady=10)

    def display_process_info(self):
        """ Display the list of running processes """
        processes = get_system_processes()
        self.output_text.delete("1.0", "end")  # Clear previous output
        self.output_text.insert("end", f"{'PID':<10}{'Process Name':<25}{'CPU%':<10}{'Memory%'}\n")
        self.output_text.insert("end", "-" * 50 + "\n")
        for proc in processes:
            self.output_text.insert("end",
                                    f"{proc['pid']:<10}{proc['name']:<25}{proc['cpu_percent']:<10}{proc['memory_percent']}\n")
        self.output_text.see("end")

    def detect_deadlock(self):
        """ Simulate deadlock detection """
        self.output_text.insert("end", "\n🔹 Deadlock Detection Initiated...\n")
        """Simulate deadlock detection output."""
        detect_resource_contention()
        with open("deadlock_prevention_output.txt", "r", encoding="utf-8") as file:
            output_text = file.read()
        file.close()
        self.output_text.insert("end", output_text)
        self.output_text.see("end")

    def check_system_safety(self):
        """ Simulate checking system safety """
        self.output_text.insert("end", "\n🔹 Checking System Safety...\n")
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

    def resolve_deadlock(self):
        """ Simulate resolving deadlocks """
        self.output_text.insert("end", "\n✅ Deadlock Recovery Completed!\n")
        deadlocks = detect_deadlocks()  # Detect actual deadlocks
        output = resolve_deadlock(deadlocks)  # Resolve if found
        self.output_text.insert("end", output + "\n")
        self.output_text.see("end")

    def apply_resources(self):
        """ Apply user-defined available resources """
        try:
            self.default_available = list(map(int, self.available_var.get().strip('[]').split(',')))
            self.default_max_demand = eval(self.max_demand_var.get())
            self.default_allocation = eval(self.allocation_var.get())
            self.output_text.insert("end", f"\n✅ Resource Values Updated!\n")
        except ValueError:
            self.output_text.insert("end", "\n❌ Invalid Resource Format! Use correct formatting.\n")

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = ProcessMonitorApp()
    app.mainloop()