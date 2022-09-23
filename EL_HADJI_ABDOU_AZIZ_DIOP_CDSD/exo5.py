def bissextile(a):
    if(a%4==0 and a%100!=0 or a%400==0):
        return "l'année ",a," est bissextile"
    else:
        return "l'année ",a," n'est pas bisextile"

print(bissextile(2038))
print(bissextile(2038))
    
