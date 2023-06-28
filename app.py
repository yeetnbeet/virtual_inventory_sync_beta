import csv
from msilib.schema import Error
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

def check_for_zeros(ID,QUANT):
    zeros=[]
    for row in ID:
        flag = False
        for item in QUANT:
            if row[1] == item[1] and row[4] == item[4] and row[2] == item[2]:
                flag = True
        if flag == False:
            zeros.append([row[-1],0])
    return zeros


def check_for_zeros_list(ID, QUANT):
    zeros = [[row[-1], 0] for row in ID if not any(
        row[1] == item[1] and row[4] == item[4] and row[2] == item[2] for item in QUANT)]

    return zeros

def phase_one():
    ID,QUANT = read_csv()
    changes = output_changes(ID,QUANT)
    for item in changes:
        update_virtual_inventory(item[0],item[1])

def phase_two():
    ID,QUANT = read_csv()
    zeros = check_for_zeros_list(ID,QUANT)
    
    for item in zeros:
        update_virtual_inventory(item[0],item[1])
        print(item)
        

if __name__ == "__main__":
    try:
        phase_one()
    except Error:
        print("Phase One")
    else:
        phase_two()
        
        

    
    

    
