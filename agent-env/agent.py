from environment import *
from time_constraint import *
from room_constraint import *
from Day import Day
from LectureRoom import LectureRoom
from csv_process import writeCsvFile
import random

dayDomain = [ Day(i) for i in range(5) ]
timeDomain = [ 9 + i for i in range(8) ]

# 담헌 실학관을 제해준다.
theoryRoomDomain = roomsForTheory[:-1]
practiceRoomDomain = roomsForPractice

def rotate(lst, n):
    return lst[-n:] + lst[:-n]

# 강의시간을 배정한다.
# @param
# subject : 과목
# room : 강의실
# @return
# 배정에 성공한 경우 True를 반환한다.
def assignTime(subject, room):
    random.shuffle(dayDomain)

    for day in dayDomain:
        # 실습 과목일 경우, 이론 수업과 다른 날짜인가?
        if subject.isPractice and isSameAsTheory(subject, day):
            continue

        for i in range(50):
            time = random.choice(timeDomain)
            
            # 점심시간인가?
            if isNoon(time):
                continue

            # 해당 시간에 강의실을 사용할 수 있는가?
            if canAssign(room, day, time, subject):
                room.assignSubject(day, time, subject)
                subject.setStartTime(day, time)
                return True
    return False

# 강의실을 배정한다.
# @param
# domain : 사용 가능한 강의실
# subject : 넣을 과목
# isPractice : 실습 과목을 배정하는 것인가?
# @return
# 배정에 성공하면 True를 반환한다.
def assignRoom(domain, subject):
    if subject.lectureRoom:
        return assignTime(subject, subject.lectureRoom)

    random.shuffle(domain)
    for room in domain:
        # 강의실이 수용할 수 있는가?
        if hasMoreCapacity(subject, room) == False:
            continue

        # 시간을 배정한다.
        if assignTime(subject, room):
            return True
    return False

# 해당 과목에 강의 시간과 강의실을 배정한다.
# @param
# subject : 과목
# @return
# 배정이 성공했다면 True를 반환한다.
def processSubject(subject):
    # 이론 과목인 경우
    if not subject.isPractice:
        # 공학설계 및 졸업설계 과목은 배치하지 않는다.
        if isDesignSubject(subject):
            return True

        # 선호 1번
        if assignRoom(theoryRoomDomain, subject):
            return True
    
    return assignRoom(practiceRoomDomain, subject)

# 이론 과목에 대해서 먼저 배치한다.
for (name, subject) in theorySubjects.items():
    if not processSubject(subject):
        subject.printDetail()
print("------------Theory Done---------------")

# 그다음 실습 과목에 대해서 배치한다.
for (name, subject) in practiceSubjects.items():
    if not processSubject(subject):
        subject.printDetail()
print("------------Practice Done---------------")


lines = Subject.toListForCsv(theorySubjects, practiceSubjects)
#writeCsvFile("Result1.csv", lines)
#writeCsvFile("Result2.csv", lines)
writeCsvFile("Result3.csv", lines)