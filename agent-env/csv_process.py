import csv

def writeCsvFile(filename, lines):
    filename = "./Result/" + filename
    with open(filename, 'w', encoding = 'utf-8', newline = '') as f:
        wr = csv.writer(f)
        for line in lines:
            wr.writerow(line)

def readCsvFile(filename):
    filename = './Data/' + filename
    d = []
    with open(filename, 'r') as f:
        rdr = csv.reader(f)
        for line in rdr:
            d.append(line)
    return d

subjectData = readCsvFile('SubjectData.csv')
lectureRoomData = readCsvFile('LectureRoomData.csv')

if __name__ == "__main__":
    for line in subjectData:
        print(line)
    print('------------------------------')
    for line in lectureRoomData:
        print(line)

    writeCsvFile("Result1.csv", subjectData)