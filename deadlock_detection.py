import psutil

def detect_resource_contention():
    """ Detects potential deadlocks by checking resource contention """
    resource_locks = {}
    
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            open_files = proc.info['open_files']
            if open_files:
                for file in open_files:
                    resource_locks.setdefault(file.path, []).append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    deadlocks = {res: pids for res, pids in resource_locks.items() if len(pids) > 1}
    
    if deadlocks:
        print("\n⚠️ Possible Deadlock Detected! Conflicting Resources:")
        for res, pids in deadlocks.items():
            print(f"Resource: {res} | Conflicting Processes: {pids}")
        return deadlocks
    else:
        print("\n✅ No Deadlocks Detected.")
        return None

if __name__ == "__main__":
    detect_resource_contention()
