# Get the number of processes
n = int(input('Enter number of processes: '))
# Get the arrival times for each process
at = list(map(int, input(f'Enter arrival times for {n} processes: ').split()))
# Get the burst times for each process
bt = list(map(int, input(f'Enter burst times for {n} processes: ').split()))
# Get the time quantum
tq = int(input('Enter time quantum: '))

# Initialize remaining burst times, current time, waiting times, and turnaround times
remaining_bt = bt.copy()
t = 0
wt = [0] * n
tat = [0] * n

# Loop until all processes are done
while True:
    done = True
    for i in range(n):
        if remaining_bt[i] > 0:
            done = False
            if remaining_bt[i] > tq:
                # Process is not finished, increment time and reduce remaining burst time
                t += tq
                remaining_bt[i] -= tq
            else:
                # Process is finished, increment time and calculate waiting time
                t += remaining_bt[i]
                wt[i] = t - bt[i] - at[i]
                remaining_bt[i] = 0
    if done:
        break

# Calculate turnaround times
for i in range(n):
    tat[i] = bt[i] + wt[i]

# Print the results
print('Process	Burst Time	Waiting Time	Turnaround Time')
for i in range(n):
    print(f'{i+1}	{bt[i]}		{wt[i]}		{tat[i]}')

# Calculate and print average waiting time and turnaround time
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f'Average Waiting Time: {avg_wt}')
print(f'Average Turnaround Time: {avg_tat}')