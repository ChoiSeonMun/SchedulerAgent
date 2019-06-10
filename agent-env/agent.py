from environment import *
from time_constraint import *
from room_constraint import *
from Day import Day
from LectureRoom import LectureRoom
from csv_process import writeCsvFile

dayDomain = [ Day(i) for i in range(5) ]
roomDomain = lectureRoomsForSorting
timeDomain = [ 9 + i for i in range(8) ]

def processTheorySubject(subject):
    # 공학설계 및 졸업설계 과목은 배치하지 않는다.
    if isDesignSubject(subject):
        return True

    for (cap, room) in roomDomain:
        # 강의실이 수용할 수 있는가?
        if hasMoreCapacity(subject, room) == False:
            continue
        for day in dayDomain:
            for time in timeDomain:
                # 점심시간인가?
                if isNoon(time):
                    continue

                # 해당 시간에 강의실을 사용할 수 있는가?
                if canAssign(room, day, time, subject):
                    lectureRoom = lectureRooms[room]
                    lectureRoom.assignSubject(day, time, subject)
                    subject.setStartTime(day, time)
                    return True
    return False

def processPracticeSubject(subject):
    for (cap, room) in roomDomain:
        # 실습실인가?
        if not canPractice(room):
            continue
        
        # 강의실이 수용할 수 있는가?
        if hasMoreCapacity(subject, room) == False:
            continue

        for day in dayDomain:
            # 이론 수업과 다른 날짜인가?
            if isSameAsTheory(subject, day):
                continue

            for time in timeDomain:
                # 점심시간인가?
                if isNoon(time):
                    continue

                # 해당 시간에 강의실을 사용할 수 있는가?
                if canAssign(room, day, time, subject):
                    lectureRoom = lectureRooms[room]
                    lectureRoom.assignSubject(day, time, subject)
                    subject.setStartTime(day, time)
                    return True
    return False

# 이론 과목에 대해서 먼저 배치한다.
for (name, subject) in theorySubjects.items():
    if not processTheorySubject(subject):
        subject.printDetail()
print("------------Theory Done---------------")

# 그다음 실습 과목에 대해서 배치한다.
for (name, subject) in practiceSubjects.items():
    if not processPracticeSubject(subject):
        subject.printDetail()
print("------------Practice Done---------------")

#for (name, subject) in theorySubjects.items():
#    subject.printDetail()

lines = Subject.toListForCsv(theorySubjects, practiceSubjects)
writeCsvFile("Result1.csv", lines)