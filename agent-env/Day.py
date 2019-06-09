from enum import Enum

class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4

    @staticmethod
    def getName(day):
        if day == Day.MON:
            return "월"
        elif day == Day.TUE:
            return "화"
        elif day == Day.WED:
            return "수"
        elif day == Day.THU:
            return "목"
        else:
            return "금"
