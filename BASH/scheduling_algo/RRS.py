from collections import deque

n = int(input('Enter number of processes: '))
at = list(map(int, input(f'Enter arrival times for {n} processes: ').split()))
bt = list(map(int, input(f'Enter burst times for {n} processes: ').split()))
tq = int(input('Enter time quantum: '))

remaining_bt = bt.copy()
wt = [0] * n
tat = [0] * n
ct = [0] * n
queue = deque()
t = 0
i = 0
visited = [False] * n

while i < n and at[i] <= t:
    queue.append(i)
    visited[i] = True
    i += 1

while queue:
    current = queue.popleft()
    exec_time = min(tq, remaining_bt[current])
    
    t += exec_time
    remaining_bt[current] -= exec_time

    if remaining_bt[current] > 0:
        queue.append(current)
    else:
        ct[current] = t
        tat[current] = ct[current] - at[current]
        wt[current] = tat[current] - bt[current]

    while i < n and at[i] <= t:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
        i += 1

print('Process\tBurst Time\tWaiting Time\tTurnaround Time')
for i in range(n):
    print(f'{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}')

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f'Average Waiting Time: {avg_wt}')
print(f'Average Turnaround Time: {avg_tat}')



"""
Round Robin Scheduling (RRS) is a preemptive CPU scheduling algorithm designed for time-sharing systems.
Each process is assigned a fixed time quantum in a cyclic order. If a process does not finish execution
within its time quantum, it is placed at the end of the queue, and the CPU moves to the next process.

RRS ensures fair allocation of CPU time to all processes, preventing starvation and improving response time,
especially for short jobs. However, if the time quantum is too small, it may lead to excessive context switching.
If too large, it behaves like First-Come-First-Served (FCFS). Choosing the right time quantum is key to achieving
a balance between responsiveness and efficiency.
"""
