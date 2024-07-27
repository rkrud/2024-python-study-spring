# [문제]
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# [입력]
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# [출력]
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

S = input().upper()
# print(S)
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

num = [] # 각 알파벳의 사용횟수 리스트
for i in alphabet:
    count_num = S.count(i)
    num.append(count_num)

# print(num)
# print(num.count(max(num)))
    
max_num = max(num) # 가장많이 사용된 알파벳의 사용횟수
max_num_index = num.index(max_num) # 가장 많이 사용된 알파벳의 사용횟수의 index 값
max_alphabet= alphabet[max_num_index] # 가장 많이 사용된 알파벳
if num.count(max_num) >= 2:
    print("?")
else:
    print(max_alphabet)
