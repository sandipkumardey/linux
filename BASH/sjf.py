def main():
    n = int(input("Enter the number of processes: "))

    processes = []  # List to store [Process ID, Arrival Time, Burst Time]

    for i in range(n):
        print(f"Enter the arrival time (AT) of process {i + 1}: ")
        at = int(input())
        print(f"Enter the burst time (BT) of process {i + 1}: ")
        bt = int(input())
        processes.append([i + 1, at, bt])  # Process ID starts from 1

    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])

    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    total_time = 0
    completed_processes = 0

    while completed_processes < n:
        shortest_job = -1
        min_burst = float('inf')

        # Find the process with the shortest burst time that has arrived and not completed
        for i in range(n):
            if not completed[i] and processes[i][1] <= total_time and processes[i][2] < min_burst:
                shortest_job = i
                min_burst = processes[i][2]

        if shortest_job == -1:
            total_time += 1
            continue

        # Execute the shortest job
        waiting_time[shortest_job] = total_time - processes[shortest_job][1]
        turnaround_time[shortest_job] = waiting_time[shortest_job] + processes[shortest_job][2]
        total_time += processes[shortest_job][2]
        completed[shortest_job] = True
        completed_processes += 1

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print results
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


if __name__ == "_main_":
    main()