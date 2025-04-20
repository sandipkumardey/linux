n = int(input("Enter number of processes: "))
print()
at = [int(input(f"Enter arrival time for P{i + 1}: ")) for i in range(n)]
print()
bt = [int(input(f"Enter burst time for P{i + 1}: ")) for i in range(n)]

processes = list(range(n))
wt = [0] * n
tat = [0] * n
completion_time = [0] * n

remaining_processes = [(i, at[i], bt[i]) for i in range(n)]
current_time = min(at)
executed_processes = []

while remaining_processes:
    available = [p for p in remaining_processes if p[1] <= current_time]
    
    if not available:
        current_time = min(p[1] for p in remaining_processes)
        continue
    
    process = min(available, key=lambda x: x[2])
    pid = process[0]
    
    completion_time[pid] = current_time + process[2]
    
    tat[pid] = completion_time[pid] - at[pid]
    wt[pid] = tat[pid] - bt[pid]
    
    current_time = completion_time[pid]
    remaining_processes.remove(process)
    executed_processes.append(process)

total_wt = sum(wt)
total_tat = sum(tat)

print("\nProcesses | Arrival | Burst | Waiting | Turnaround")
print("-" * 50)
for i in range(n):
    print(f"{i + 1:^9} | {at[i]:^7} | {bt[i]:^5} | {wt[i]:^7} | {tat[i]:^10}")
print("-" * 50)
print(f"\nAverage waiting time = {total_wt / n:.2f}")
print(f"Average turnaround time = {total_tat / n:.2f}")




"""
SJF (Shortest Job First) is a CPU scheduling algorithm that selects the process
with the shortest burst time among the available processes at the current time.
It is non-preemptive, meaning once a process starts execution, it runs till
completion.

SJF minimizes the average waiting time and turnaround time but may lead to
starvation if short processes keep arriving and long ones are delayed. Unlike FCFS,
SJF considers burst time, making it more efficient in many cases, especially for
batch systems with known job lengths.
"""