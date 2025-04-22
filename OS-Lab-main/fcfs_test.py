n = int(input("Enter the number of processes: "))
at, bt = [], []

for i in range (n):
    at.append(int(input(f"Enter arrival time of process p{i}: ")))

for i in range (n):
    bt.append(int(input(f"Enter burst time of process p{i}: ")))

wt = [0] * n
ct = [0] * n
tat = [0] * n

ct[0] = at[0] + bt[0]
tat[0] = ct[0] - at[0]
wt[0] = tat[0] - bt[0]

for i in range (1, n):
    ct[i] = max(ct[i-1], at[i]) + bt[i]
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

avg_tat = sum(tat) // n
avg_wt = sum(wt) // n

print("\nPID\tArrival Time\tBurst Time\tCompletion Time\t\tTurn Arround Time\tWaiting Time\n")
for i in range (n):
    print(f"\np{i}\t{at[i]}\t\t{bt[i]}\t\t\t{ct[i]}\t\t\t{tat[i]}\t\t\t{wt[i]}\n")