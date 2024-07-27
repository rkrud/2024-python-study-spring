# 리스트 []

subway = [10, 20, 30]
print(subway)
subway = ["이가경", "삼가경", "사가경"]
print(subway)

# 삼가경씨가 몇 번째 칸에 타고 있는가?
print(subway.index("삼가경"))

# 오가경씨가 다음 정류장에서 다음 칸에 탐
subway.append("오가경")
print(subway)

# 육가경씨를 삼가경 사가경 사이에 태워봄
subway.insert(1, "육가경")
print(subway)

# 지하철에 있는 사람을  한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는 지 확인
subway.append("이가경")
print(subway)
print(subway.count("이가경"))

# 정렬
num_list = [9, 8, 2, 1, 4]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [9, 8, 2, 1, 4]
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)