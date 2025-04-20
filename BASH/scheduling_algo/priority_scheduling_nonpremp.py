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

remaining_processes = [(i, at[i], bt[i], priority[i]) for i in range(n)]
current_time = min(at)
executed_processes = []

while remaining_processes:
    available = [p for p in remaining_processes if p[1] <= current_time]
    
    if not available:
        current_time = min(p[1] for p in remaining_processes)
        continue
    
    process = min(available, key=lambda x: (x[3], x[1]))
    pid = process[0]
    
    completion_time[pid] = current_time + process[2]
    
    tat[pid] = completion_time[pid] - at[pid]
    wt[pid] = tat[pid] - bt[pid]
    
    current_time = completion_time[pid]
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
Non-Preemptive Priority Scheduling is a CPU scheduling algorithm where each process is assigned a priority,
and the CPU is allocated to the process with the highest priority (lower numerical value = higher priority).
Unlike the preemptive version, once a process starts execution, it runs to completion—even if a higher
priority process arrives during its execution.

This approach is simpler and incurs less overhead due to the absence of context switching. However, it can
lead to higher average waiting times and response times for more urgent processes if they arrive after
a lower-priority process has already started. It is best suited for batch systems or scenarios where
preemption is undesirable.

The program simulates the execution of all processes by selecting from the available ones based on priority,
calculating waiting time, turnaround time, and their averages for performance evaluation.
"""
