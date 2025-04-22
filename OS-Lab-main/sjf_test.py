n = int(input("Enter the number of processes: "))
at, bt = [], []

for i in range (n):
    at.append(int(input(f"Enter arrival time of process p{i}: ")))

for i in range (n):
    bt.append(int(input(f"Enter burst time of process p{i}: ")))

wt = [0] * n
tat = [0] * n
ct = [0] * n

rp = []
for i in range (n):
    rp.append((at[i], bt[i], i))

current_time = min(at)

while rp:

    available_process = []
    for i in range (len(rp)):
        if rp[i][0] <= current_time:
            available_process.append(rp[i])
        
    if not available_process:
        current_time = min(rp)[0]
        continue

    process = min(available_process, key=lambda x: x[1])
    pid = process[2]
    ct[pid] = current_time + process[1]
    tat[pid] = ct[pid] - at[pid]
    wt[pid] = tat[pid] - bt[pid]
    current_time = ct[pid]
    rp.remove(process)

print("\nPID\tArrival Time\tBurst Time\tCompletion Time\t\tTurn Arround Time\tWaiting Time\n")
for i in range (n):
    print(f"\np{i}\t{at[i]}\t\t{bt[i]}\t\t\t{ct[i]}\t\t\t{tat[i]}\t\t\t{wt[i]}\n")