jours=[1,2,3,4,5,6,7,8,9,10,11,12]
trente=30
trente_et_un=31
annee=int(input("entrer une année non bissextile : "))

if(annee%4==0 and annee%100!=0 or annee%400==0):
        print("l'année est bissextile veuillez entrer une année non bissextile")
else:
    for i  in (jours):
        if(jours[1]or jours[3]or jours[5]or jours[7]or jours[9]or jours[10]or jours[12]):
            print(f"{jours[i]} est {trente_et_un} ")
        elif(jours[2]or jours[4]or jours[6] or jours[8]or jours[11]):
            print(f"{jours[i]} est {trente} ")


        
