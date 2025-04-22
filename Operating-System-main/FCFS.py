def fcfs(n, at, bt):
    ct, wt, tt = [0] * n, [0] * n, [0] * n
    ct[0] = at[0] + bt[0]
    tt[0] = bt[0]
    wt[0] = 0
    for i in range(1, n):
        ct[i] = max( ct[i-1], at[i]) + bt[i]
        tt[i] = ct[i] - at[i]
        wt[i] = tt[i] - bt[i]

    return {"AVG WT": sum(wt) / n, "AVG TAT": sum(tt) / n}

