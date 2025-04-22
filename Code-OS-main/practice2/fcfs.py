n = int(input("Enter the number of processes: "))

at, bt = [], []

for i in range(n):
    at.append(int(input(f"Enter the arrival time of process P{i}: ")))

for i in range(n):
    bt.append(int(input(f"Enter the burst time of process P{i}: ")))
    
wt = [0] * n
ct = [0] * n
tat = [0] * n

ct[0] = at[0] + bt[0]

for i in range(1, n):
    ct[i] = max(ct[i - 1], at[i]) + bt[i]
    wt[i] = ct[i] - at[i] - bt[i]

for i in range(n):
    tat[i] = bt[i] + wt[i]

total_wt = sum(wt)
total_tat = sum(tat)

print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i}\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    
print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
    
