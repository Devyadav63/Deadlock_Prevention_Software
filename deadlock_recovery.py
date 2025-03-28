import psutil

def terminate_process(pid):
    """ Terminates a process by PID """
    try:
        process = psutil.Process(pid)
        process.terminate()
        return f"✅ Terminated Process: {pid} ({process.name()})"
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return f"❌ Failed to terminate Process {pid}"


def resolve_deadlock(deadlocks):
    """ Recovers from detected deadlocks by terminating processes """
    if not deadlocks:
        return "✅ No Deadlocks Found.\n"

    output = "\n⚡ Initiating Deadlock Recovery...\n"
    for resource, pids in deadlocks.items():
        output += f"🔴 Killing Process {pids[0]} to free {resource}\n"
        output += terminate_process(pids[0]) + "\n"
    output += "\n✅ Deadlock resolved!\n"
    return output

# if __name__ == "__main__":
#     deadlocks = {
#         "/tmp/locked_file.txt": [1234, 5678]  # Simulated deadlock scenario
#     }
#     resolve_deadlock(deadlocks)
#     print("\n🔒 Deadlock Recovery Check Complete.")
#     print("🔍 System Monitoring and Deadlock Recovery Completed.")
#

