
print("######## exo1 ######")
x= 20
n=-4
avoir_n_chiffres= True
if(x >0 and n > 0):
    print(avoir_n_chiffres)
else:
    avoir_n_chiffres= False
    print(avoir_n_chiffres)
print("######## exo2 ######")
L= [81,-12,0,-81,-31]
M= [-81,12,0,81,31]
sontOpposees= True
i=0
while(i<len(L) and i<len(M)):
    if(L[i]==M[i]):
        sontOpposees=False
        print(L[i]," et ",M[i],"-> ",sontOpposees)
    else:
         sontOpposees=True
         print(L[i]," et ",M[i],"-> ",sontOpposees)
    i+=1
print("######## exo3 ######")
def est_monotone():
    F=[5,5,6,6,6,10]
    v=True
    for i in range(len(F)):
        if(F[i]<F[i+1] or F[i]>F[-1] or F[i]==F[i]):
            v= True
            print(F[i],'->',v)
        else:
            v= False
            print(F[i],'->',v)
est_monotone()
