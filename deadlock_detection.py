import psutil

def detect_deadlocks():
    """Detects potential deadlocks by checking for blocked processes."""
    deadlocks = {}
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        try:
            if proc.info['status'] == psutil.STATUS_STOPPED:  # Simulate checking for blocked processes
                deadlocks[f"Resource-{proc.pid}"] = [proc.pid]
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return deadlocks
def detect_resource_contention():
    """ Detects potential deadlocks by checking resource contention and logs the output to a file """
    resource_locks = {}
    output_lines = []

    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            open_files = proc.info['open_files']
            if open_files:
                for file in open_files:
                    resource_locks.setdefault(file.path, []).append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    deadlocks = {res: pids for res, pids in resource_locks.items() if len(pids) > 1}

    with open("deadlock_prevention_output.txt", "w", encoding="utf-8") as file:  # ✅ Added encoding="utf-8"
        if deadlocks:
            output_lines.append("\n⚠️ Possible Deadlock Detected! Conflicting Resources:\n")
            for res, pids in deadlocks.items():
                line = f"Resource: {res} | Conflicting Processes: {pids}"
                output_lines.append(line)
                print(line)  # Print to console
        else:
            output_lines.append("\n✅ No Deadlocks Detected.")
            print("\n✅ No Deadlocks Detected.")

        file.write("\n".join(output_lines))  # Write output to file

    return deadlocks if deadlocks else None


if __name__ == "__main__":
    detect_resource_contention()
    print("\n📄 Output saved to deadlock_prevention_output.txt")
