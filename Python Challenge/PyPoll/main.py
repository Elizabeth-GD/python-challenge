import os
import csv

csvpath = os.path.join("election_data_review.csv")
candidate = []

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  reader=next(csvreader)

  for row in csvreader:
      candidate.append(row[2]) 

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(candidate)))
print("----------------------------")

Khan = candidate.count("Khan")
khanpercent = int((Khan) / len(candidate) * 100)
print("Khan: " + str(khanpercent) + "% (" + str(Khan) + ")")

Correy = candidate.count("Correy")
correypercent = int((Correy) / len(candidate) * 100)
print("Corry: " + str(correypercent) + "% (" + str(Correy) + ")")

Li = candidate.count("Li")
Lipercent = int((Li) / len(candidate) * 100)
print("Li: " + str(Lipercent) + "% (" + str(Li) + ")")

OTooley = candidate.count("O'Tooley")
OTooleypercent = int((OTooley) / len(candidate) * 100)
print("O'Tooley " + str(OTooleypercent) + "% (" + str(OTooley) + ")")

print("----------------------------")

if khanpercent > .50:
	print("Winner: Khan")
elif correypercent > .50:
	print("Winner: Correy")
elif Lipercent > .50:
	print("Winner: Li")
else:
	print("Winner: O'Tooley")			

f = open("scumbagstats.txt","w")   
f.write("Khan: " + str(khanpercent) + "% (" + str(Khan) + ")")
f.write("Corry: " + str(correypercent) + "% (" + str(Correy) + ")")
f.write("Li: " + str(Lipercent) + "% (" + str(Li) + ")")
f.write("O'Tooley " + str(OTooleypercent) + "% (" + str(OTooley) + ")")
f.close()		