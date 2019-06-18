#Cerco il max del vettore (O(n))

a=[13, 1, 5, 12, 45, 4, 2, 3, 2]
#a=[1,2,2,3,4,5,12,13,45]
b=[0]*len(a)
m = max(a)

#CountingSort
def CountingSort(A, B, max):
    C=[]
    C=[0]*(max+1)
    for j in range(0, len(A)):
        C[A[j]]=C[A[j]]+1
    # Ho registrato il numero di copie che ho di ogni numero
    for i in range(1, max+1):
        C[i]=C[i]+C[i-1]
    #C[i] contiene tutti i numeri <= i
    for j in range(len(A)-1, -1, -1):
          B[C[A[j]]-1] = A[j]
          C[A[j]] = C[A[j]] - 1
    return B

print(CountingSort(a,b,m))

a=127
print((a//10)%10)

#TODO domanda al prof: quindi uso sempre 24 bytes?

a=139709808099
def RadixSort(A,p):
    if A%p == 0:
      r=len(A)/p
    else:
      r=round((len(A)/p)+1)
    #ho appena definito il numero di volte che il ciclo verra ripetuto

    for i in range(1,r):
        #TODO prendo i*p numeri
        #TODO ciclare sui numeri
        #TODO fare funzione per prendere l'iesima cifra
        a=10