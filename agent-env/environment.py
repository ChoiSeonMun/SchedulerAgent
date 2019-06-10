from csv_process import subjectData, lectureRoomData
from LectureRoom import *
from Subject import Subject

theorySubjects = {}
practiceSubjects = {}
roomsForTheory = []
roomsForPractice = []

# 해당 과목이 공학설계 혹은 졸업설계 과목인지 판단한다.
# @param
# subject : 과목
# @return
# 해당 과목이 공학설계 혹은 졸업설계면 True 반환
def isDesignSubject(subject):
    if "캡스톤디자인" in subject.name:
        return True
    return False

# 과목을 전처리한다.
# @param
# data : SubjectData에 있는 데이터
def preprocessSubject(data):
    isPractice = True if data[2] != "0" else False

    # 강의실이 미리 배정되어 있다면
    # 해당되는 인스턴스를 찾는다.
    lectureRoom = None
    if data[-2] != "" and data[-2] != "X":
        for r in roomsForPractice:
            if data[-2] == r.name:
                lectureRoom = r
                break
        # 위에서 찾지 못했다면
        # 해당 과목은 정보보호개론 or 산업체취창업특강이므로
        # 담헌실학관 102호를 넣어준다
        if lectureRoom == None:
            lectureRoom = roomsForTheory[-1]

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
        practice = Subject(
            name = data[0],
            time = int(data[2]),
            isPractice = True,
            number = data[3],
            capacity = int(data[4]),
            lectureRoom = lectureRoom,
            startTime = None
        )
        practiceSubjects[practice.ID] = practice

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

    if lectureRoom.canPractice:
        roomsForPractice.append(lectureRoom)
    else:
        roomsForTheory.append(lectureRoom)

for room in lectureRoomData[1:]:
    preprocessRoom(room)

for subject in subjectData[1:]:
    preprocessSubject(subject)

if __name__ == "__main__":
    print("------------------TheoryRoom-------------------")
    for r in roomsForTheory:
        r.printDetail()
        print("---------------------")

    print("------------------PracticeRoom-------------------")
    for r in roomsForPractice:
        r.printDetail()
        print("---------------------")

    print("------------------TheorySubject----------------")
    for k, v in theorySubjects.items():
        v.printDetail()
        print("---------------------")
    print("------------------PracticeSubject---------------")
    for k, v in practiceSubjects.items():
        v.printDetail()
        print("---------------------")