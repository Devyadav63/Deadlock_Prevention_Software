import psutil

def terminate_process(pid):
    """ Terminates a process by PID """
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"✅ Terminated Process: {pid} ({process.name()})")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"❌ Failed to terminate Process {pid}")

def resolve_deadlock(deadlocks):
    """ Recovers from detected deadlocks by terminating processes """
    print("\n⚡ Initiating Deadlock Recovery...")
    for resource, pids in deadlocks.items():
        print(f"🔴 Killing Process {pids[0]} to free {resource}")
        terminate_process(pids[0])
    print("\n✅ Deadlock resolved!")

if __name__ == "__main__":
    deadlocks = {
        "/tmp/locked_file.txt": [1234, 5678]  # Simulated deadlock scenario
    }
    resolve_deadlock(deadlocks)
    print("\n🔒 Deadlock Recovery Check Complete.")
    print("🔍 System Monitoring and Deadlock Recovery Completed.")
  

