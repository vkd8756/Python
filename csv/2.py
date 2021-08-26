import csv
with open('innovators.csv', 'w',newline='') as file:
    write = csv.writer(file)
    write.writerow(["SN", "Name", "Contribution","Value"])
    write.writerow([1, "Linus Torvalds", "Linux Kernel",20])
    write.writerow([2, "Tim Berners-Lee", "World Wide Web",40])
    write.writerow([3, "Guido van Rossum", "Python Programming",70])
with open('innovators.csv') as csvfile:
    data=list(csv.DictReader(csvfile))
for i in data:
    print(i["Value"])
print(data[0].keys())
