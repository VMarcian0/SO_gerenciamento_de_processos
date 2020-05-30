# Python3 programa para implementação do  
# Escalonamento Round Robin   
  
# Função para encontrar o tempo de espera para todos os processos
def findWaitingTime(processes, n, bt, wt, quantum):  
    rem_bt = [0] * n 
  
    # Copy the burst time into rt[]  
    for i in range(n):  
        rem_bt[i] = bt[i] 
    t = 0 # Current time  
  
    # Mantem a circulação da fila enquanto os processos não estão todos concluidos  
    while(1): 
        done = True
  
        # Mudar os processos um a um
        for i in range(n):
            # Se o tempo de execução é maior que zero significa que ele não terminou    
            if (rem_bt[i] > 0) : 
                done = False
                  
                if (rem_bt[i] > quantum) : 
                    # Aumentando o valor de t indica a quanto tempo o processo está sendo executado
                    t += quantum  
                    # Reduzir o tempo estimado por uma unidade de quantum
                    rem_bt[i] -= quantum  
                  
                # Se o tempo estimando é menor ou igual a unidade de quantum o processo está terminado
                else: 
                  
                    # Increase the value of t i.e. shows  
                    # how much time a process has been processed  
                    t = t + rem_bt[i]  
  
                    # Waiting time is current time minus  
                    # time used by this process  
                    wt[i] = t - bt[i]  
  
                    # Quando o processo terminar marcar o tempo estimado de execução para zero
                    rem_bt[i] = 0
                  
        # Se todos os processos estão terminados está pronto  
        if (done == True): 
            break
              
# Function to calculate turn around time  
def findTurnAroundTime(processes, n, bt, wt, tat): 
      
    # Calculating turnaround time  
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
  
  
# Function to calculate average waiting  
# and turn-around times.  
def findavgTime(processes, n, bt, quantum):  
    wt = [0] * n 
    tat = [0] * n  
  
    # Function to find waiting time 
    # of all processes  
    findWaitingTime(processes, n, bt,  
                         wt, quantum)  
  
    # Function to find turn around time 
    # for all processes  
    findTurnAroundTime(processes, n, bt, 
                                wt, tat)  
  
    # Display processes along with all details  
    print("Processes    Burst Time     Waiting",  
                     "Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", i + 1, "\t\t", bt[i],  
              "\t\t", wt[i], "\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = %.5f "% (total_tat / n))  
      
# Driver code 
# Main 
if __name__ =="__main__": 
      
    # Ids dos processos  
    proc = [1, 2, 3] 
    # Qauntidade de processos
    n = 3
  
    # Burst time of all processes
    # Tempo que cada processo vai levar em unidades de quantum
    burst_time = [10, 5, 8]  
  
    # Time quantum
    # Quantas unidades de tempo serão utilizdas por processo por execução
    quantum = 2;  
    findavgTime(proc, n, burst_time, quantum) 
  
# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
# Esse código foi traduzido e explanado por
# Victor Marciano (Marcian0)