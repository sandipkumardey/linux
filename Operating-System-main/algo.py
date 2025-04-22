def fcfs_scheduling(processes):
    # Sort processes by arrival time (ascending order)
    processes.sort(key=lambda x: x[0])

    # Initialize total waiting time and turnaround time
    twt = 0  # Total waiting time
    ttt = 0  # Total turnaround time
    ct = 0   # Completion time (tracks when each process finishes execution)

    # Iterate through each process
    for pid, at, bt in processes:  # Using 'at' for arrival time, 'bt' for burst time
        # If the CPU is idle, move to the arrival time of the current process
        if ct < at:
            ct = at

        # Waiting time = time when process starts execution - its arrival time
        wt = ct - at  # Waiting time

        # Turnaround time = waiting time + burst time
        tt = wt + bt  # Turnaround time

        # Update completion time as the process finishes execution
        ct += bt

        # Accumulate total waiting and turnaround time for average calculation
        twt += wt
        ttt += tt

        # Print waiting time and turnaround time for each process
        print(f"Process {pid}: Waiting Time = {wt}, Turnaround Time = {tt}")

    # Print average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {twt / len(processes):.2f}")
    print(f"Average Turnaround Time: {ttt / len(processes):.2f}")

# Example Usage
process_list = [
    (1, 0, 5),  # Process 1 arrives at time 0, requires 5 units of CPU time
    (2, 1, 3),  # Process 2 arrives at time 1, requires 3 units of CPU time
    (3, 2, 8) # Process 4 arrives at time 3, requires 6 units of CPU time
]

# Call the function to execute FCFS scheduling
fcfs_scheduling(process_list)

#