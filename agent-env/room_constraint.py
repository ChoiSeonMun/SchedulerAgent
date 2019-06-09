from Subject import Subject
from LectureRoom import LectureRoom
from environment import lectureRooms
from Day import Day

# 강의실이 해당 과목의 인원을 수용할 수 있는지 검사한다.
# @pamam
# subject : 과목
# roomName : 강의실 이름
# @return
# 수용할 수 있으면 True를 반환한다.
def hasMoreCapacity(subject, roomName):
    room = lectureRooms[roomName]
    return room.capacity >= subject.capacity

# 강의실이 실습실인지 검사한다.
# @param
# roomName : 강의실 이름
# @return
# 해당 강의실이 실습실이면 True를 반환한다.
def canPractice(roomName):
    room = lectureRooms[roomName]
    return room.canPractice

# 특정 시간에 강의실을 이용할 수 있는지 검사한다.
# @param
# roomName : 강의실 이름
# day : 날짜
# start : 시작시간
# time : 강의시간
def canAssign(roomName, day, start, time):
    if start == 12:
        return False

    room = lectureRooms[roomName]
    timeTable = room.getAvailableTimeTable(day)
    for i in range(time):
        if start + i not in timeTable:
            return False
    return True

if __name__ == "__main__":
    tempRoom = LectureRoom("테스트 강의실", 104, 25, False)
    lectureRooms["테스트 강의실"] = tempRoom
    tempSubj = Subject("테스트", 2, True, 1, 40, None, "수14")

    print("hasMoreCapacity")
    print("--------------------")
    print("Expected False, Real:", hasMoreCapacity(tempSubj, "테스트 강의실"))
    
    print("canPractice")
    print("--------------------")
    print("Expected False, Real:", canPractice("테스트 강의실"))

    print("canAssign")
    print("--------------------")
    start = 9
    tempSubj2 = Subject("테스트2", 2, False, 1, 25, None, None)
    tempRoom.assignSubject(Day.TUE, start, tempSubj2)
    print("Expected False, Real:", canAssign("테스트 강의실", Day.TUE, 10, 2))
    print("Expected True, Real:", canAssign("테스트 강의실", Day.TUE, 11, 2))

