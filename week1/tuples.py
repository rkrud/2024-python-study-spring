# tuple
# list와의 차이점: 
# 단점: 내용을 변경하거나 추가할 수 없음. 
# 장점: list보다 속도가 더 빠르다

menu = ("돈까스", "치즈까스")
print(menu[0])

print(menu[1])

name = "이가경"
age = 24
hobby = "헬스"
print(name, age, hobby)

(name, age, hobby) = ("이가경", 24, "헬스")
print(name, age, hobby)
