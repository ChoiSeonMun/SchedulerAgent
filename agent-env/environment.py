from data import classData, classRoomData

classDataCategory = classData[0]
classRoomCategory = classRoomData[0]

subjects = { }
rooms = { }

def hasPractice(subject):
    return subject[2] != "0"

def isDesignSubject(code):
    designCode = [ "공학설계", "졸업설계" ]
    for i in designCode:
        if i in code:
            return True
    return False

def printDetail(item):
    print(item)
    detail = subjects[item] if item in subjects else rooms[item]
    for (k, v) in detail.items():
        print(str.format("{}: {}", k, v))

def preprocessSubject(subject):
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

def preprocessRoom(room):
    name = room[-1]
    detail = {
        "lectureroom": room[0],
        "capacity": room[1],
        "isLab": True if room[2] == "o" else False,
        "time": []
    }
    rooms[name] = detail

for subject in classData[1:]:
    preprocessSubject(subject)
for room in classRoomData[1:]:
    preprocessRoom(room)

for subject in subjects:
    printDetail(subject)

print("==========================================")
for room in rooms:
    printDetail(room)