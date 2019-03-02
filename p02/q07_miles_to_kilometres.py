table = "Miles\tKilometres\tKilometres\tMiles\n"
for i in range(1,11):
    table1 += "{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}\n".format(i,i*1.609,(i+3)*5,(i+3)*5/1.609)
    
print(table)