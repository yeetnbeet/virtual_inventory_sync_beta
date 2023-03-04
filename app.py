import csv
from helpers import update_virtual_inventory

LOCATIONID = 55834411176

def read_csv():
    ID = []
    QUANT = []
    with open('ID.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ID.append(row)
    with open('QUANT.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            QUANT.append(row)

    return ID , QUANT

def output_changes(ID,QUANT):
    changes = []
    for row in ID:
        for i in QUANT:
            if row[1] == i[1] and row[4] == i[4] and row[2] == i[2]:
                changes.append([row[-1],i[6]])
    for item in changes:
        if item[1] == "+10":
            item[1] = "10"
    return changes


if __name__ == "__main__":
    ID,QUANT = read_csv()
    changes = output_changes(ID,QUANT)
    for item in changes:
        update_virtual_inventory(item[0],item[1])

    
