# without any functions
n = int(input("Enter number of processes: "))
at = [int(input(f"Enter arrival time for process {i + 1}: ")) for i in range(n)]
bt = [int(input(f"Enter burst time for process {i + 1}: ")) for i in range(n)]

wt = [0] * n
service_time = [0] * n
service_time[0] = at[0]

for i in range(1, n):
    service_time[i] = service_time[i - 1] + bt[i - 1]
    wt[i] = max(0, service_time[i] - at[i])

tat = [bt[i] + wt[i] for i in range(n)]
total_wt = sum(wt)
total_tat = sum(tat)

print("Processes Arrival Burst Waiting Turnaround")
for i in range(n):
    print(f"{i + 1}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")
print(f"\nAverage waiting time = {total_wt / n:.5f}")
print(f"Average turnaround time = {total_tat / n:.5f}")
