import csv

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