class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ : 생성자
# 마린이나 탱크같은 객체가 생성될 때 자동으로 호출되는 부분
# 객체: 클래스로 부터 만들어지는 것, 마린과 탱크는 Unit class의 isinstance이다.