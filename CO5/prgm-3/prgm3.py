import csv
list=[]
with open('whoknows.csv','r')as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        list.append(line)
print(list)
