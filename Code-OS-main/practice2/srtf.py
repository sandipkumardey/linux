n = int(input("Enter the number of processes: "))

at = [int(input(f"Enter the arrival time of process {i+1}: ")) for i in range(n)]
bt = [int(input(f"Enter the burst time of process {i+1}: ")) for i in range(n)]

wt, ct, tat = [0] * n, [0] * n, [0] * n
remaining_bt = bt.copy()
completed = [False] * n
current_time = 0
completed_processes = 0

while completed_processes < n:
    # Find the process with the minimum remaining time that has arrived
    min_remaining_time = float('inf')
    min_index = -1
    for i in range(n):
        if at[i] <= current_time and not completed[i] and remaining_bt[i] < min_remaining_time:
            min_remaining_time = remaining_bt[i]
            min_index = i

    if min_index != -1:
        # Process found, update times
        current_time += remaining_bt[min_index]
        ct[min_index] = current_time
        tat[min_index] = ct[min_index] - at[min_index]
        wt[min_index] = tat[min_index] - bt[min_index]
        completed[min_index] = True
        completed_processes += 1
        remaining_bt[min_index] = 0
    else:
        # No process is currently available, increment time
        current_time += 1
        
        
# Display results
print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tCompletion Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{ct[i]}\t\t{tat[i]}")
    
print("\nAverage Waiting Time:", sum(wt) / n)
print("Average Turnaround Time:", sum(tat) / n)

