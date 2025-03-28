def is_safe_state(available, max_demand, allocation):
    """ Checks if the system is in a safe state using Banker's Algorithm """
    num_processes = len(allocation)
    num_resources = len(available)

    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        allocated = False
        for i in range(num_processes):
            if not finish[i] and all(max_demand[i][j] - allocation[i][j] <= work[j] for j in range(num_resources)):
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                allocated = True
                break
        if not allocated:
            return False, []

    return True, safe_sequence

