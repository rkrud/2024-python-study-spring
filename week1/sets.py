# 집합 (set)
# 중복 불가, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"이가경", "삼가경", "사가경"}
python = set(["이가경", "오가경"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가
python.add("육가경")
print(python)

# 제거
java.remove("육가경")
print(java)
