# # 지역변수와 전역변수
# 지역변수: 함수 내에서만 쓸 수 있는 변수
# 전역변수: 프로그램 내에서 모든 곳에서 쓸 수 있는 변수

# checkpoint_error 함수는 오류가 발생. 함수 안의 지역변수인 gun이 초기화 되어있지 않기 때문.

# gun = 10

# def checkpoint_error(soldiers): 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint_error(2)
# print("남은 총: {0}".format(gun))

# checkpoint 함수 밖에서는 gun의 값이 변하지 않음(지역변수)
# gun = 10

# def checkpoint(soldiers): 
#     gun = 20 #지역변수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint(2)
# print("남은 총: {0}".format(gun))

gun = 10

def checkpoint(soldiers): 
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

# 전역변수는 권장되는 방법은 아님, 따라서 아래와 파라미터를 이용한 방법을 많이  사용
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun


print("전체 총: {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))