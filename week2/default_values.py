# 기본값

def profile(name, age, main_lang):
    print("이름 :{0}\t 나이: {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

def profile(name, age=17, main_lang = "파이썬"):
    print("이름 :{0}\t 나이: {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

profile("이가경")
profile("삼가경")
