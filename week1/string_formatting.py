print('a' + 'b')
print("a", "b")

# 방법 1
print("나는 %d살 입니다. " % 20)
print("나는 %s을 좋아해요 " % "파이썬") 
print("Apple 은 %c로 시작해요 " % "A") 

# %s
print("나는 %s살 입니다. " % 20)
print("나는 %s을 좋아해요 " % "파이썬")
print("Apple 은 %s로 시작해요 " % "A")
print("나는 %s 색과 %s 색을 좋아해요" %("파란", "노란"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "노란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "노란"))

# 방법 4 (v3.6 이상~)
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")