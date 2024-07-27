for waiting in [0, 1, 2, 3, 4]:
    print("대기번호: {0}".format(waiting))

for waiting in range(5): # 0, 1, 2, 3, 4
    print("대기번호: {0}".format(waiting))

for waiting in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호: {0}".format(waiting))

shop = ["이가경", "삼가경", "사가경"]
for customer in shop:
    print("{0}님 음료 나왔습니다".format(customer))