# 표준입출력

# print("A", "B", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

import sys
print("A", "B", file=sys.stdout) #표준출력
print("A", "B", file=sys.stderr) #표준에러: log처리 할때 표준 에러부분 따로 로딩해서 에러 처리할 수 있음 

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8): 8칸 확보 후 왼쪽 정렬, rjust(4): 4칸 확보 후 오른 쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(n): n만큼의 공간을 확보하고 값이 없는 빈 공간에 대해서는 0을 넣음

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer)) # 사용자 입력을 통해 값을 받게 되면 문자열형태로 저장
