unit_info = {
    "probe":{
        "name":"probe",
        "mineral":50,
        "gas":0,
        "hp":20,
        "shield":20,
        "demage":5

    },
    "zealot":{
        "name":"zealot",
        "mineral":100,
        "gas":0,
        "hp":100,
        "shield":60,
        "demage":16
    },
    "dragoon":{
        "name":"dragoon",
        "mineral":125,
        "gas":50,
        "hp":100,
        "shield":80,
        "demage":20
    }
}
class Unit:
    def __init__(self, name, hp, shield, demage):
     self.name = name
     self.hp = hp
     self.shield = shield
     self.demage = demage
    
class Player:
    def __init__(self, nikname, mineral, gas, unit_list=[]):
        self.nikname = nikname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list
    def produce(self, name, mineral, gas, hp, shield, demage):
        if self.mineral - mineral < 0:
            print("미네랄이 부족합니다")
        elif self.gas - gas < 0:
            print("가스가 부족합니다")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, demage)
            self.unit_list.append(unit)
            print(f"[{name}] 을(를) 생산합니다.")

player1 = Player("Bisu", 500, 200)

player1.produce(unit_info['probe']['name'], unit_info['probe']['mineral'], unit_info['probe']['gas'], unit_info['probe']['hp'], unit_info['probe']['shield'], unit_info['probe']['demage'])
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'], unit_info['zealot']['gas'], unit_info['zealot']['hp'], unit_info['zealot']['shield'], unit_info['zealot']['demage'])
player1.produce(unit_info['dragoon']['name'], unit_info['dragoon']['mineral'], unit_info['dragoon']['gas'], unit_info['dragoon']['hp'], unit_info['dragoon']['shield'], unit_info['dragoon']['demage'])

for unit in player1.unit_list:
    print(f"[{unit.name}] 체력: {unit.hp} 방어막: {unit.shield} 공격력: {unit.demage}")
