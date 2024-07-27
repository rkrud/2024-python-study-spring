# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "이가경", main_lang="파이썬", age = 20) # 매개변수의 값을 키워드를 이용해 함수를 호출하면 키워드의 값의 순서가 섞여있어도 전달됨
profile("이가경", main_lang="파이썬", age = 20, name="삼가경")