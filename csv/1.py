#with open(food.csv) as csvfile:
#    lst=list(csv.DictReader(csvfile))
#print(lst[:3])
#import alpha.txt
#import alpha.txt
j=open('alpha.txt','r')
for i in j:
    print(i)
with open('alpha.txt') as file:
    data=file.read()
print(data)
import csv
with open('food.csv') as csvfile:
    data=list(csv.DictReader(csvfile))
print(data[:3][:2])
