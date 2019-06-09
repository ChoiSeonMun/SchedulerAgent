from data import classData

subjects = { }

def hasPractice(subject):
    return subject[2] != "0"

def isDesignSubject(code):
    designCode = [ "공학설계", "졸업설계" ]
    for i in designCode:
        if i in code:
            return True
    return False

def printDetail(subject):
    print(subject)
    detail = subjects[subject]
    for (k, v) in detail.items():
        print(str.format("{}: {}", k, v))

def preprocessData(subject):
    name = str.format("{}-{}-T", subject[0], subject[3])
    detail = {
        "time" : int(subject[1]),
        "capacity" : int(subject[4]),
        "professor" : subject[-3],
        "classroom" : subject[-2],
        "start" : subject[-1]
    }
    subjects[name] = detail

    if isDesignSubject(name) == False and hasPractice(subject):
        practicename = name[:-1] + "P"
        detail["time"] = int(subject[2])
        subjects[practicename] = detail


for i in range(1, len(classData)):
    subject = classData[i]
    preprocessData(subject)
