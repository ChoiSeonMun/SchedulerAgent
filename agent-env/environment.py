from data import subjectData, lectureRoomData
from LectureRoom import *
from Subject import Subject

theorySubjects = {}
practiceSubjects = {}
lectureRooms = {}
lectureRoomsForSorting = []

# 해당 과목이 설계 과목인지 판단한다.
# @param
# subject : 과목
# @return
# 해당 과목이 설계 과목이면 True 반환
def isDesignSubject(subject):
    designSubject = [ "공학설계", "졸업설계" ]
    if subject.name in designSubject:
        return True
    return False

# 과목을 전처리한다.
# @param
# data : SubjectData에 있는 데이터
def preprocessSubject(data):
    isPractice = True if data[2] != "0" else False
    lectureRoom = lectureRooms[data[-2]] if data[-2] != "" and data[-2] != "X" else None

    # 이론 과목
    subject = Subject(
        name = data[0],
        time = int(data[1]),
        isPractice = False,
        number = data[3],
        capacity = int(data[4]),
        lectureRoom = lectureRoom,
        startTime = data[-1]
    )
    theorySubjects[subject.ID] = subject

    # 실습 과목
    if isDesignSubject(subject) == False and isPractice:
        subject.time = int(data[2])
        subject.isPractice = True
        subject.startTime = None
        practiceSubjects[subject.ID] = subject

# 강의실을 전처리한다.
# @param
# data : LectureRoomData에 있는 데이터    
def preprocessRoom(data):
    lectureRoom = LectureRoom(
        name = data[-1],
        number = data[0],
        capacity = int(data[1]),
        canPractice = True if data[2] == "o" else False
    )
    lectureRooms[lectureRoom.name] = lectureRoom
    lectureRoomsForSorting.append((lectureRoom.capacity, lectureRoom.name))

for room in lectureRoomData[1:]:
    preprocessRoom(room)
lectureRoomsForSorting.sort()

for subject in subjectData[1:]:
    preprocessSubject(subject)

if __name__ == "__main__":
    print("------------------Room-------------------")
    for k, v in lectureRooms.items():
        v.printDetail()
    for room in lectureRoomsForSorting:
        print(room)

    print("------------------TheorySubject----------------")
    for k, v in theorySubjects.items():
        v.printDetail()
        print("---------------------")
    print("------------------PracticeSubject---------------")
    for k, v in practiceSubjects.items():
        v.printDetail()
        print("---------------------")