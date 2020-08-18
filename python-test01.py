

a=10
b=1
print(a+b)



var = '''hello world'''

print(var)

print(var[0])

# print(var[15])

print(var.split()) # 자르기.... 공백기준?

var2 = """   HELLO       """


print(var2.rstrip()) # 우측 공백 제거
print(var2.lstrip()) # 좌측 공백 제거
print(var2.strip()) # 양측 공백 제거


var0 = 'i am' + ' 홍길동'
var00 = 'i am {name}'.format(name='홍길동')
var000 = 'i am {0}'.format("""홍길동""")
var0000 = 'i am {0} ㅁㅁㅁ {name}'.format("홍길동" , name = "정보 문화사")
var00000 = 'i am {0} , {1}'.format("홍길동" , "ㅅㅅㅅㅅ")

print(var0)
print(var00)
print(var000)
print(var0000)
print(var00000)

list1 = ['a','c','e','d']

list1.sort()

print(list1)

list1.sort(reverse=True)

print(list1)



c1 = False

c2 = False

c3 = True


if c1:
    print("1")
elif c2:
    print("2")
elif c3:
    print("3")


signal = input("색을 영문으로 입력해주세요 : ")

if signal == 'blue':
    print("파란색입니다 지나가세요")
elif signal == 'red':
    print("빨간색입니다 멈추세요")
elif signal == 'yellow':
    print("노란색입니다 기다리세요")
else:
    print("이상한 색입니다")


cnt = 0

while cnt<5:

    print("while %d번째"%(cnt))
    cnt+=1


for i in range(0, 5):
    print("for %d번쨰"%(i))

for i in "hello":

    print(i)

for i in [11,22,33,44,55]:

    print(i)

var = {"key1":"value1", "key2":"value2"}

for key in var:
    print(key)
    print(var[key])

print("")

strr = """지난 이틀간 수도권과 강원 등 중북부 지방이 고비였다면, 오늘과 내일 주의해야 할 지역은 바로 충청과 남부 지역인데요,

이 지역에는 내일까지 벼락을 동반한 시간당 30~50mm의 장대비가 쏟아질 것으로 보입니다.

추가 호우피해 발생하지 않도록 주의하셔야겠습니다.

현재 레이더 화면을 보면 얇고 길게 발달한 강한 비구름이 전남과 경남 지역에 걸쳐 있습니다.

울산에는 호우경보가 내려진 가운데 시간당 65mm의 장대비가 쏟아지고 있고요,

호우주의보가 내려진 전남과 경남 곳곳에 시간당 10~20mm의 강한 비가 집중되고 있습니다.

서울은 현재 비가 소강상태를 보이고 있지만,

차츰 서해 상에서 유입되는 비구름의 영향을 받겠고요,

출근길 무렵에는 비가 시작될 것으로 예상됩니다.

지금까지 철원 동송읍에 755mm의 전국에서 가장 많은 비가 내렸고요,

서울 도봉구에도 403mm의 많은 비가 내렸습니다.

내일까지 경기 남부와 영서 남부, 충청과 남부 내륙에 많은 곳은 300mm 이상의 호우가 쏟아지겠고요,

남해안에 150mm 이상, 수도권과 그 밖의 지역에 50~100mm의 비가 내리겠습니다.

이에 따라 오늘 오전 남해안을 시작으로 오후에는 충청과 그 밖의 남부 지방에 호우특보가 내려지겠고요,

경기 남부와 강원 남부 지역에도 오늘 밤에는 호우특보가 발효되겠습니다.

이번 주말 내내 전국 대부분 지역에 비가 이어지겠고요,

중북부 지방의 비는 다음 주 후반까지 길게 이어지겠습니다.

기상센터였습니다."""


space = strr.split(" ")

frequency = {}

for char in space:
    frequency.setdefault(char,0)
    frequency[char]+=1
    print(frequency)


def f(x):
    return x+10

gg = f(5)

print(gg)

print("")

def division(x):
    if x%2 == 0:
        return True
    else:
        return False

    print("running")

v1 = division(10)
v2 = division(11)

print(v1)
print(v2)

print("")

def xx(x,y):
    print('running' + str(x) + ' ' + str(y))
    return True

va1 = xx(10,11)
print(va1)

print("")

def xxx(x,y=20):
    print('running'+str(x)+str(y))
    return x+y

v1 = xxx(55) # y=20 처리 x+y
v2 = xxx(55,10) # y 값 들어있는 x+y

print(v1)
print(v2)


print("")

class charactor:


    def create(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def move(self):
        print(self,"move")

    def attack(self):
        print(self,"attack")

    def show_info(self):
        print("hp : %d, attack : %d, defence : %d" %(self.hp , self.attack, self.defence))


playa = charactor()
playa.move()
playa.attack()
playa.create(10,20,30)
playa.show_info()

playb = charactor()
playb.move()
playb.attack()
playb.create(100,200,3000)
playb.show_info()

print("")


class ch:

    def __init__(self, hp, attack, defence): #생성자
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("플레이어가 생성되었습니다")

    def __call__(self):
        print("hp : %d" %(self.hp))

    def show_info(self):
        print("hp : %d, attack : %d, defence : %d" % (self.hp, self.attack, self.defence))
        
    def __del__(self): #소멸자
        print("플레이어가 죽었습니다")


        

pa = ch(10,20,30)
pa.show_info()
pb = ch(111,123,123132)
pb.show_info()

pa()
pb()

print(callable(pa)) # 실행 가능한지 판별


del pa
del pb


print("")

class space:

    # 스태틱 메소드를 이용하면 클래스를 객체생성 도구가 아닌 목적으로 가능.
    # 객체가 없어 self 인자를 받지 않음

    @staticmethod
    def s1():
        print("s1 스태틱메소드")

print("")

# 클래스 변수 << 클래스에서 변수를 만들 때 독립적으로 변수를 부여. 클래스 변수에 접근 할 땐 self 인자가 아닌 클래스 이름.클래스변수 로 접근

class cnt:

    cnt = 0

    def __init__(self, hp):
        self.info = {

            'hp' : hp

        }

        cnt.cnt +=1;

        print("생성된 수 : %d"%(cnt.cnt))


z1 = cnt(10)
z2 = cnt(10)
z3 = cnt(10)

print(cnt.cnt)




# 상속

print("")


class unit:
    unit_cnt = 0

    def __init__(self):
        print("unit 생성")
        unit.unit_cnt += 1


    def move(self):
        print("unit move")


class bird(unit):
    def __init__(self):
        print("bird 생성")
        super(bird,self).__init__() # 첫번째 인자는 자식 클래스이름 , 두번째 인자는 self


b1 = bird()

b1.move()

print(unit.unit_cnt) # unit의 unit_cnt가 정상적으로 실행되지 않는 현상 발생 << super를 이용해

