n = int(input("Enter number of processes: "))
at = [int(input(f"Enter arrival time for process {i + 1}: ")) for i in range(n)]
bt = [int(input(f"Enter burst time for process {i + 1}: ")) for i in range(n)]

processes = sorted(range(n), key=lambda x: (at[x], bt[x]))

wt = [0] * n
tat = [0] * n
service_time = at[processes[0]]

for i in range(1, n):
    service_time += bt[processes[i - 1]]
    wt[processes[i]] = max(0, service_time - at[processes[i]])

tat = [bt[i] + wt[i] for i in range(n)]

print("Processes    Arrival Burst Waiting Turnaround")
for i in processes:
    print(f"{i + 1}\t\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")
print(f"\nAverage waiting time = {sum(wt) / n:.5f}")
print(f"Average turnaround time = {sum(tat) / n:.5f}")
