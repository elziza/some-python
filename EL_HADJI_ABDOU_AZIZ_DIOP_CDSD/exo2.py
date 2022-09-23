L=[4,2,2,4]
f=0
for i in range(len(L)):
    f=L[i]+1
    if(L[i]==f):
        print(f"la liste {L} est en miroir")
       
    else:
        print(f"la liste {L} n'est pas en miroir")
        