def srtf(processes):
    """ Implements Shortest Remaining Time First (Preemptive SJF) Scheduling """

    # Sort processes by arrival time initially
    processes.sort(key=lambda x: x[0])

    current_time = 0
    tat, twt = 0, 0
    remaining_time = {p[2]: p[1] for p in processes}  # Track remaining burst time
    completion_time = {}  # Track completion time
    n = len(processes)

    while remaining_time:
        # Get processes that have arrived by the current time
        available_processes = [p for p in processes if p[0] <= current_time and p[2] in remaining_time]

        if available_processes:
            # Select process with the shortest remaining burst time
            process = min(available_processes, key=lambda x: remaining_time[x[2]])
        else:
            # If no process is available, move CPU time forward
            process = min(processes, key=lambda x: x[0])
            current_time = process[0]

        # Extract process details
        at, bt, pid = process

        # CPU executes for 1 unit (preemption possibility)
        remaining_time[pid] -= 1
        current_time += 1

        # If process finishes execution, remove it from tracking
        if remaining_time[pid] == 0:
            completion_time[pid] = current_time  # Store completion time
            wt = completion_time[pid] - at - bt  # Corrected Waiting Time Formula
            tt = completion_time[pid] - at  # Turnaround Time

            twt += wt
            tat += tt

            del remaining_time[pid]  # Process completed, remove it

    # Compute final averages
    avg_wt = twt / n
    avg_tat = tat / n

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

# Example Usage
process_list = [(0, 16, 0), (1, 5, 1), (2, 6, 2), (3, 1, 3), (4, 2, 4)]
srtf(process_list)