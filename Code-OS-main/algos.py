def fcfs(at, bt, n):
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    tat[0] = bt[0]
    ct[0] = at[0] + bt[0]

    for i in range(1, n):
        ct[i] = bt[i] + max(ct[i - 1], at[i])
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))


def sjf(at, bt, n):
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    remProcess = [(i, at[i], bt[i]) for i in range(n)]
    currTime = min(at)

    while remProcess:
        availableProcess = [process for process in remProcess if process[1] <= currTime]

        if not availableProcess:
            currTime = min(process[1] for process in remProcess)
            continue

        process = min(availableProcess, key=lambda x: x[2])
        processID = process[0]
        ct[processID] = currTime + process[2]
        currTime = ct[processID]

        remProcess.remove(process)

    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))


def srtf(at, bt, n):
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    remainTime = bt.copy()
    completed = 0
    isComplete = [False] * n
    currTime = min(at)

    while completed < n:
        minRemainTime = float("inf")
        selected = -1

        for i in range(n):
            if at[i] <= currTime and not isComplete[i]:
                if remainTime[i] < minRemainTime:
                    minRemainTime = remainTime[i]
                    selected = i

        if selected == -1:
            currTime += 1
            continue

        remainTime[selected] -= 1

        if remainTime[selected] == 0:
            ct[selected] = currTime + 1
            isComplete[selected] = True
            completed += 1

        currTime += 1

    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))


def rrs(at, bt, n, tq):
    remTime = bt.copy()
    currTime = min(at)
    
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    
    while True:
        done = True
        
        for i in range(n):
            if remTime[i] > 0:
                done = False
                
                if remTime[i] > tq:
                    remTime[i] -= tq
                    currTime += tq
                else:
                    currTime += remTime[i]
                    ct[i] = currTime
                    remTime[i] = 0
                    
        if done:
            break
        
    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        
    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))


def priorityNonPreemptive(at, bt, n, pr):
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    remProcess = [(i, at[i], bt[i], pr[i]) for i in range(n)]
    currTime = min(at)
    
    while remProcess:
        availableProcess = [process for process in remProcess if process[1] <= currTime]
        
        if not availableProcess:
            currTime = min(process[1] for process in availableProcess)
            continue
        
        process = min(availableProcess, key=lambda x: (x[3], x[1]))
        processID = process[0]
        ct[processID] = currTime + process[2]
        currTime = ct[processID]
        
        remProcess.remove(process)
        
    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        
    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))
        

def priorityPreemptive(at, bt, n, pr):
    ct, wt, tat = [0] * n, [0] * n, [0] * n
    remainTime = bt.copy()
    currTime = min(at)
    completed = 0
    isComplete = [False] * n
    
    while completed < n:
        minPriority = float('inf')
        selected = -1
        
        for i in range(n):
            if at[i] <= currTime and not isComplete[i]:
                if remainTime[i] > 0 and pr[i] < minPriority:
                    minPriority = pr[i]
                    selected = i
                    
        if selected == -1:
            currTime += 1
            continue
        
        remainTime[selected] -= 1
        
        if remainTime[selected] == 0:
            ct[selected] = currTime + 1
            isComplete[selected] = True
            completed += 1
            
        currTime += 1
        
    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        
    return (round((sum(wt) / n), 2), round((sum(tat) / n), 2))

n = int(input("Enter number of processes: "))
at = [int(input(f"Enter arrival time of process {i + 1}: ")) for i in range(n)]
bt = [int(input(f"Enter burst time of process {i + 1}: ")) for i in range(n)]
pr = [int(input(f"Enter priority of process {i + 1}: ")) for i in range(n)]
tq = int(input("Enter time quantum for Round Robin: "))

print("FCFS:", fcfs(at, bt, n))
print("SJF:", sjf(at, bt, n))
print("SRTF:", srtf(at, bt, n))
print("RR:", rrs(at, bt, n, tq))
print("Priority Non-Preemptive:", priorityNonPreemptive(at, bt, n, pr))
print("Priority Preemptive:", priorityPreemptive(at, bt, n, pr))

