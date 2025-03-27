from system_monitor import display_process_info
from deadlock_detection import detect_resource_contention
from deadlock_prevention import is_safe_state
from deadlock_recovery import resolve_deadlock

def main():
    print("\n🔹 Step 1: System Monitoring")
    display_process_info()

    print("\n🔹 Step 2: Detecting Deadlocks")
    deadlocks = detect_resource_contention()

    if True:  # Force deadlock recovery for testing

        print("\n🔹 Step 3: Checking System Safety (Deadlock Prevention)")
        available = [3, 3, 2]  
        max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
        allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

        safe, sequence = is_safe_state(available, max_demand, allocation)
        if safe:
            print(f"\n✅ System is Safe. Safe Sequence: {sequence}")
        else:
            print("\n❌ Deadlock Risk Detected! Proceeding to Recovery.")

            print("\n🔹 Step 4: Resolving Deadlocks")
            resolve_deadlock(deadlocks)
    else:
        print("\n✅ No Deadlock Recovery Needed.")

if __name__ == "__main__":
    main()
    print("\n🔒 System Monitoring and Deadlock Management Completed.")