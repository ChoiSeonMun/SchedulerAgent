import csv

def readCsvFile(filename):
    filename = './Data/' + filename
    d = []
    with open(filename, 'r') as f:
        rdr = csv.reader(f)
        for line in rdr:
            d.append(line)
    return d

classData = readCsvFile('classData.csv')
classRoomData = readCsvFile('classRoomData.csv')

if __name__ == "__main__":
    for line in classData:
        print(line)
    print('------------------------------')
    for line in classRoomData:
        print(line)