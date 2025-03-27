import psutil

def get_system_processes():
    """ Fetch running processes and their resource usage """
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_info = proc.info
            processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes

def display_process_info():
    """ Display the list of running processes """
    processes = get_system_processes()
    print(f"{'PID':<10}{'Process Name':<25}{'CPU%':<10}{'Memory%'}")
    print("-" * 50)
    for proc in processes:
        print(f"{proc['pid']:<10}{proc['name']:<25}{proc['cpu_percent']:<10}{proc['memory_percent']}")

if __name__ == "__main__":
    display_process_info()
