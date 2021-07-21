import csv

with open("height-weight.csv", newline = "") as f :
    reader = csv.reader(f)
    file_data = list(reader)

#To remove the title from the data
file_data.pop(0)
new_data = []

#sorting data to get only height of people
for i in range(len(file_data)) :
    h = file_data[i][1]
    new_data.append(float(h))

#Finding mean
n = len(new_data)
sum = 0
for s in new_data :
    sum = sum + s

mean = sum/n
print(mean)