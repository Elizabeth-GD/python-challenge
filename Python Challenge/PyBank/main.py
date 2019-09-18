import csv as csv
import os as os
totalBalance = 0
averageChange = 0
totalDates = 0
var_historico_max = 0
var_historico_min = 0
var_anterior_valor = 0
var_gap = 0
var_counter = 0
csv_path = os.path.join("budget_data_bank.csv")
with open(csv_path, 'r', ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:      
        totalBalance += int(row[1])
        if var_counter > 0:
            var_gap = (int(row[1]) - var_anterior_valor)
            averageChange = var_gap  + averageChange        
            var_anterior_valor = int(row[1])            
            if var_gap > var_historico_max:
                var_historico_max = var_gap
                rowMax = row
            if var_gap < var_historico_min:            
                var_historico_min = var_gap
                rowMin = row
        else:
            var_anterior_valor = int(row[1])
        var_counter += 1
averageChange = averageChange / (var_counter - 1)  

print(f"Total Months: {var_counter}")        
print(f"Total: {totalBalance}")
print(f"Average change: {averageChange}")
print(f"Greates increase in profits: {rowMax[0]} ({var_historico_max})")
print(f"Greates decrease in profits: {rowMin[0]} ({var_historico_min})")

output_path = os.path.join("salida.txt")

with open(output_path, 'w') as txtFile:
  
    print(f"Total Months: {totalDates}", file = txtFile)        
    print(f"Total: {totalBalance}", file = txtFile)
    print(f"Average change: {averageChange}", file = txtFile)
    print(f"Greates increase in profits: {rowMax[0]} ({var_historico_max})", file = txtFile)
    print(f"Greates decrease in profits: {rowMin[0]} ({var_historico_min})", file = txtFile)