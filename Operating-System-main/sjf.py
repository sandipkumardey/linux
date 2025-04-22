def sjf_scheduling(processes):
    """ Computes Average Waiting Time (TWT) & Average Turnaround Time (TAT) for SJF Non-Preemptive Scheduling """

    # Sort processes by arrival time initially
    processes.sort(key=lambda x: x[0])

    current_time = 0
    total_wt, total_tat = 0, 0
    num_processes = len(processes)  # Store original number of processes before modifying the list

    while processes:
        # Get processes that have arrived by current time
        available_processes = [p for p in processes if p[0] <= current_time]

        if available_processes:
            # Pick the process with the shortest burst time
            process = min(available_processes, key=lambda x: x[1])
        else:
            # If no process is available, move time forward to the next arriving process
            process = min(processes, key=lambda x: x[0])
            current_time = process[0]

        # Extract process details
        at, bt, pid = process

        # Compute waiting time & turnaround time
        wt = current_time - at
        tat = wt + bt

        # Update total waiting time & turnaround time
        total_wt += wt
        total_tat += tat

        # Update current time & remove executed process
        current_time += bt
        processes.remove(process)

    # Compute averages using the stored `num_processes`
    avg_wt = total_wt / num_processes
    avg_tat = total_tat / num_processes

    return avg_wt, avg_tat

# Example Usage
process_list = [(0, 16, 0), (1, 5, 1), (2, 6, 2), (3, 1, 3), (4, 2, 4)]
average_wt, average_tat = sjf_scheduling(process_list)

print(f"\nAverage Waiting Time: {average_wt:.2f}")
print(f"Average Turnaround Time: {average_tat:.2f}")