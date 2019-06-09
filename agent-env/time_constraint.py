from Subject import Subject
from Day import Day
from environment import theorySubjects

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

# 모든 제약조건을 만족하는지 확인한다.
# @param
# subject : 실습 과목
# day : 날짜
def canAssign(subject, day):
    return not isSameAsTheory(subject, day)

if __name__ == "__main__":
    tempSubj = Subject("테스트 과목1", 0, False, 0, 0, None, "수14")
    theorySubjects[tempSubj.ID] = tempSubj
    print("isSameAsTheoryTest")
    print("Expected True, Real:", isSameAsTheory(tempSubj, Day.WED))
    print("-------------------------------")
