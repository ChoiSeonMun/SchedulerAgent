from Day import Day
from csv_process import subjectData
from environment import *

class Subject:
    def __init__(self, name, time, isPractice, number, capacity, lectureRoom, startTime):
        self.name = name                # 과목명
        self.time = time                # 강의 시간
        self.isPractice = isPractice    # 실습인지의 여부
        self.number = number            # 분반
        self.capacity = capacity        # 가용인원
        self.lectureRoom = lectureRoom  # 배정된 강의실
        self.startTime = startTime      # 배정된 시작시간
        self.ID = name + str(number)
    
    # 과목의 상태를 출력한다.
    def printDetail(self):
        print("Name:", self.name)
        print("Time:", self.time)
        print("IsPractice:", self.isPractice)
        print("Number:", self.number)
        print("Capacity:", self.capacity)
        print("LectureRoom:", self.lectureRoom.name if self.lectureRoom != None else None)
        print("startTime:", self.startTime)

    def setStartTime(self, day, start):
        day = Day.getName(day)
        self.startTime = day + str(start)

    @staticmethod
    def toListForCsv(theory, practice):
        lines = []
        
        # 카테고리 추가
        lines.append(subjectData[0])
        for data in subjectData[1:]:
            # 이론 과목과 실습 과목을 가져온다.
            subjectID = data[0] + data[3]
            t = theory[subjectID]
            p = practice.get(subjectID)

            data[-2] = (t.lectureRoom.name if t.lectureRoom != None else "X") + (' ' + p.lectureRoom.name if p != None else "")
            data[-1] = t.startTime + (' ' + p.startTime if p != None else "")

            lines.append(data)

        return lines
    
