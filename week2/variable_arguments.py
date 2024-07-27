def profile(name, age, *lang):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end="  ") #end="  "를 이용하면 다음 문장이 줄바꿈 없이 출력
    for i in lang:
        print(i, end="  ")
    print()

profile("이가경", 20, "python", "java", "c")
profile("삼가경", 24, "C++")