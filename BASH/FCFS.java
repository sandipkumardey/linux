import java.util.*;

public class FCFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of processes: ");
        int n = sc.nextInt();
        int at[] = new int[n];
        int bt[] = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter the arrival time (AT) of process " + (i + 1) + ": ");
            at[i] = sc.nextInt();
            System.out.println("Enter the burst time (BT) of process " + (i + 1) + ": ");
            bt[i] = sc.nextInt();
        }

        int sumAt = 0;
        for (int i : at) {
            sumAt += i;
        }

        int sumBt = 0;
        for (int i : bt) {
            sumBt += i;
        }

        int ex[] = new int[n + 1];
        ex[0] = at[0];
        for (int i = 0; i < n; i++) {
            ex[i + 1] = ex[i] + bt[i];
        }

        int sumEx = 0;
        for (int i : ex) {  
            sumEx += i;
        }
        sumEx -= ex[n];

        float ans = ((float) sumEx - (float) sumAt) / n;
        System.out.println("The average waiting time is " + ans);

        int tatSum = 0;
        for (int i = 0; i < n; i++) {
            tatSum += ex[i + 1] - at[i];
        }
        float avgTAT = (float) tatSum / n;
        System.out.println("The average turnaround time is " + avgTAT);
    }
}