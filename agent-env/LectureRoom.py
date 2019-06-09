from Day import *

class LectureRoom:
    def __init__(self, name, number, capacity, canPractice):
        self.name = name                # 호실 이름
        self.number = number            # 호실
        self.canPractice = canPractice  # 실습가능 여부
        self.capacity = capacity        # 가용할 수 있는 인원
        self.used = {}                  # 사용현황
        self.availableTimeTable = [ [ 9 + i for i in range(8) if i != 3] for j in range(5) ] # 가용한 시간
    
    # 해당 날짜의 가용 테이블을 가져온다.
    # @param
    # day : 날짜
    def getavailableTimeTable(self, day):
        return self.availableTimeTable[day.value]

    # 해당 과목을 배치한다.
    # @param
    # day : 날짜
    # startTime : 시작 시간
    # subject : 과목
    def setClass(self, day, startTime, subject):
        dayTimeTable = self.availableTimeTable[day.value]

        self.used[Day.getName(day)] = (startTime, subject)
        for i in range(subject.time):
            dayTimeTable.delete(startTime + i)
    
    # 강의실의 상태를 출력한다.
    def printDetail(self):
        print("Name:", self.name)
        print("Number:", self.number)
        print("CanPractice:", self.canPractice)
        print("Capacity:", self.capacity)
        print("Used:", self.used)