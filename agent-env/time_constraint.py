from Subject import Subject
from Day import Day
from environment import theorySubjects

"""
시간에 대한 제약사항
1. 점심시간에는 수업이 없어야 한다.
2. 공학설계, 졸업설계의 시간은 수요일 14시 ~ 15시로 고정한다.
3. 분반이 같은 과목의 이론과 실습은 같은 날에 진행할 수 없다.
"""

# 해당 시간이 점심시간인지 판단한다.
# @param
# time : 시간
# @return
# 12시라면 True를 반환한다.
def isNoon(time):
    return time == 12

# 해당 과목의 이론이 같은 날에 진행되는지 판단한다.
# @param
# subject : 실습 과목
# day : 날짜
# @return
# 날짜가 같으면 True를 반환한다.
def isSameAsTheory(subject, day):
    theory = theorySubjects[subject.ID]
    time = theory.startTime
    return Day.getName(day) == time[0]

if __name__ == "__main__":
    tempSubj = Subject("테스트 과목1", 0, False, 0, 0, None, "수14")
    theorySubjects[tempSubj.ID] = tempSubj
    print("isSameAsTheoryTest")
    print("Expected True, Real:", isSameAsTheory(tempSubj, Day.WED))
    print("-------------------------------")
