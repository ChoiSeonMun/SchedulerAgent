from enum import Enum

# Enumeration for day
class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4

class LectureRoom:
    def __init__(self, name, number, capacity, canPractice):
        self.name = name                # 호실 이름
        self.number = number            # 호실
        self.canPractice = canPractice  # 실습가능 여부
        self.capacity = capacity        # 가용할 수 있는 인원
        self.used = None                # 사용현황
        self.availableTimeTable = [ [ 9 + i for i in range(8) if i != 3] for j in range(5) ] # 가용한 시간
    
    # 해당 날짜의 가용 테이블을 가져온다.
    # @param
    # day : 날짜
    def getavailableTimeTable(day):
        return availableTimeTable[day.value]

    # 해당 과목을 배치한다.
    # @param
    # day : 날짜
    # startTime : 시작 시간
    # subject : 과목
    def setClass(day, startTime, subject):
        dayTimeTable = availableTimeTable[day.value]
        day = day.name

        used[day] = (startTime, subject)
        for i in range(subject.time):
            dayTimeTable.delete(startTime + i)