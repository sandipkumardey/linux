n = int(input("Enter number of processes: "))
print()
at = [int(input(f"Enter arrival time for P{i + 1}: ")) for i in range(n)]
print()
bt = [int(input(f"Enter burst time for P{i + 1}: ")) for i in range(n)]
print()
priority = [int(input(f"Enter priority for P{i + 1}: ")) for i in range(n)]

processes = list(range(n))
wt = [0] * n
tat = [0] * n
completion_time = [0] * n
remaining_bt = bt[:]

remaining_processes = [(i, at[i], bt[i], priority[i]) for i in range(n)]
current_time = 0
executed_processes = []

while remaining_processes:
    available = [p for p in remaining_processes if p[1] <= current_time]
    
    if not available:
        current_time = min(p[1] for p in remaining_processes)
        continue
    
    process = min(available, key=lambda x: (x[3], x[1]))
    pid = process[0]
    
    remaining_bt[pid] -= 1
    current_time += 1
    
    if remaining_bt[pid] == 0:
        completion_time[pid] = current_time
        tat[pid] = completion_time[pid] - at[pid]
        wt[pid] = tat[pid] - bt[pid]
        remaining_processes.remove(process)
        executed_processes.append(process)

total_wt = sum(wt)
total_tat = sum(tat)

print("\nProcesses | Arrival | Burst | Priority | Waiting | Turnaround")
print("-" * 60)
for i in range(n):
    print(f"{i + 1:^8} | {at[i]:^7} | {bt[i]:^5} | {priority[i]:^8} | {wt[i]:^7} | {tat[i]:^10}")
print("-" * 60)
print(f"\nAverage waiting time = {total_wt / n:.2f}")
print(f"Average turnaround time = {total_tat / n:.2f}")



"""
Preemptive Priority Scheduling is a CPU scheduling algorithm where each process is assigned a priority,
and the CPU is allocated to the process with the highest priority (lower numerical value = higher priority).
In the preemptive version, a currently running process can be interrupted if a new process arrives with a
higher priority.

This algorithm ensures that important tasks are executed earlier, making it suitable for real-time systems
where certain operations are time-critical. It dynamically checks for process arrivals at every time unit,
allowing immediate preemption if needed. However, lower-priority processes may experience starvation if
higher-priority processes keep arriving. Aging can be introduced to avoid this, but it's not included here.

The program calculates the waiting time, turnaround time, and average of both by simulating the preemptive
priority scheduling step-by-step, making it useful for understanding how CPU decisions evolve over time.
"""