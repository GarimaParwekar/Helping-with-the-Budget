spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
count1=0
count2=0
count3=0
for spending in spendings:
    if (spending < 1000.0):
        count1+=1
    elif(spending >=1000.0 and spending <=2500.0):
        count2+=1
    else:
        count3+=1
print('Numbers of months with low spendings: ',count1)
print('Numbers of months with normal spendings: ',count2)
print('Numbers of months with high spendings: ',count3)
