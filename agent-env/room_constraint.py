from Subject import Subject
from LectureRoom import LectureRoom
from Day import Day

"""
강의실에 대한 제약사항
1. 강의실의 정원은 수강정원보다 같거나 커야 한다.
2. 수업에 따라 적절한 강의실이 배정되어야 한다.
3. 공학설계, 졸업설계의 강의실은 배정되지 않는다.
4. 각 강의실은 동일한 시간대의 과목에 대해서 중복 배치될 수 없다.
5. 강의실은 여러 과목에 분산되어 배치되어야 한다.
6. 산업체취·창업특강, 정보보호개론 외에는 담헌실학관을 사용하지 않는다.

선호
1. 이론 수업은 실습 강의실보단 이론 강의실을 택한다.
"""

# 강의실이 해당 과목의 인원을 수용할 수 있는지 검사한다.
# @pamam
# subject : 과목
# room : 강의실
# @return
# 수용할 수 있으면 True를 반환한다.
def hasMoreCapacity(subject, room):
    return room.capacity >= subject.capacity

# 특정 시간에 강의실을 이용할 수 있는지 검사한다.
# @param
# room : 강의실
# day : 날짜
# start : 시작시간
# subject : 과목
def canAssign(room, day, start, subject):
    if start == 12:
        return False

    time = subject.time
    timeTable = room.getAvailableTimeTable(day)
    for i in range(time):
        if start + i not in timeTable:
            return False
    return True

if __name__ == "__main__":
    tempRoom = LectureRoom("테스트 강의실", 104, 25, False)
    tempSubj = Subject("테스트", 2, True, 1, 40, None, "수14")

    print("hasMoreCapacity")
    print("--------------------")
    print("Expected False, Real:", hasMoreCapacity(tempSubj, tempRoom))

    print("canAssign")
    print("--------------------")
    start = 9
    tempSubj2 = Subject("테스트2", 2, False, 1, 25, None, None)
    tempRoom.assignSubject(Day.TUE, start, tempSubj2)
    print("Expected False, Real:", canAssign(tempRoom, Day.TUE, 10, 2))
    print("Expected True, Real:", canAssign(tempRoom, Day.TUE, 11, 2))

