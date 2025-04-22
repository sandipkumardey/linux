def round_robin(processes, quantum):
    twt = 0
    ttt = 0
    n = len(processes)
    current_time = 0
    queue = processes[:]  # Copy the list to avoid modifying the original
    completion_time = {}
    remaining_time = {p[2]: p[1] for p in processes}

    while remaining_time:
        for at, bt, pid in queue:
            if pid in remaining_time and at <= current_time:
                if remaining_time[pid] > quantum:
                    current_time += quantum
                    remaining_time[pid] -= quantum
                else:
                    current_time += remaining_time[pid]
                    completion_time[pid] = current_time
                    wt = current_time - at - bt
                    tt = current_time - at

                    twt += wt
                    ttt += tt
                    del remaining_time[pid]

    print(f"\nAverage Waiting Time: {twt / n:.2f}")
    print(f"Average Turnaround Time: {ttt / n:.2f}")


process_list = [(0, 5, 0), (1, 7, 1), (2, 3, 2), (3, 4, 3)]
time_quantum = 2
round_robin(process_list, time_quantum)