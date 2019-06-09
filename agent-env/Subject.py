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

    
