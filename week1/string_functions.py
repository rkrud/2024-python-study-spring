#문자열 처리 함수
python = "python is amaizing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) # python[0]이 대문자인가
print(len(python))
print(python.replace("python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 찾는 값이 없을 때 -1을 반환
# print(python.index("Java")) # 찾는 값이 없을 때 오류 발생 

print(python.count("]"))
