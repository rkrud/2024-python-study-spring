customer = "이가경"
index = 5
while index >= 1:
    print("{0} 음료 나왔습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("음료 폐기 처분되었습니다")

customer = "이가경"
person = "unknown"

while person != customer:
    print("{0}님 음료 나왔습니다".format(customer))
    person = input("이름이 어떻게 되세요?")
print("네, 가져가시면 됩니다.")