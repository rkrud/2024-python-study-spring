# key,value 값을 가진다. key에 대한 중복은 허용 X

cabinet = {3: "이가경", 100: "삼가경"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) # 오류 발생
print(cabinet.get(5)) #null값 반환

print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # 해당 키의 존재여부 확인, True
print(5 in cabinet) # False

cabinet = {"A-3" : "이가경", "B-100":"삼가경"}
print(cabinet["A-3"])
print(cabinet["B-100"])


print(cabinet)

# 새 손님
cabinet["c-20"] = "사가경"
print(cabinet)
cabinet["A-3"] = "오가경" # 값 업데이트
print(cabinet)

# 간 손님
del cabinet["A-3"]
print("?")
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)



