n = int(input("Enter number of processes: "))
print()
at = [int(input(f"Enter arrival time for P{i + 1}: ")) for i in range(n)]
print()
bt = [int(input(f"Enter burst time for P{i + 1}: ")) for i in range(n)]

remaining_time = bt.copy()
completion_time = [0] * n
current_time, completed = 0, 0
wt, tat = [0] * n, [0] * n
is_completed = [False] * n

while completed < n:
    min_remaining = float('inf')
    selected_process = -1
    
    for i in range(n):
        if at[i] <= current_time and not is_completed[i]:
            if remaining_time[i] < min_remaining:
                min_remaining = remaining_time[i]
                selected_process = i
    
    if selected_process == -1:
        current_time += 1
        continue

    remaining_time[selected_process] -= 1

    if remaining_time[selected_process] == 0:
        completion_time[selected_process] = current_time + 1
        is_completed[selected_process] = True
        completed += 1

        tat[selected_process] = completion_time[selected_process] - at[selected_process]
        wt[selected_process] = tat[selected_process] - bt[selected_process]
    
    current_time += 1

total_wt = sum(wt)
total_tat = sum(tat)

print("\nProcesses | Arrival | Burst | Waiting | Turnaround")
print("-" * 50)
for i in range(n):
    print(f"{i + 1:^9} | {at[i]:^7} | {bt[i]:^5} | {wt[i]:^7} | {tat[i]:^10}")
print("-" * 50)
print(f"\nAverage waiting time = {total_wt / n:.2f}")
print(f"Average turnaround time = {total_tat / n:.2f}")