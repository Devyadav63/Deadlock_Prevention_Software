import customtkinter as ctk
from tkinter import scrolledtext
import psutil
from system_monitor import get_system_processes



class ProcessMonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("System Process Monitor")
        self.geometry("900x600")
        ctk.set_appearance_mode("light")

        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="green", height=50)
        self.header_frame.pack(fill="x")
        self.header_label = ctk.CTkLabel(self.header_frame, text="System Process Monitor", font=("Arial", 18, "bold"),
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

        self.refresh_button = ctk.CTkButton(self.action_frame, text="Show Process List",
                                            command=self.display_process_info)
        self.refresh_button.pack(pady=10,padx=15, fill="x")

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

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = ProcessMonitorApp()
    app.mainloop()