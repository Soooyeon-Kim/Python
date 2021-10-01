# random 모듈로 로또 번호 추출하기#
# random 모듈을 활용하여 1~45사이의 7개 숫자를 생성하고 lucky_numbers 리스트에 저장

## one 
import random

LottorNumber = []
while len(LottorNumber) < 7 :
    V = random.randint(1,45)
    if V not in LottorNumber:
        LottorNumber.append(V)

print(LottorNumber)

## two
import random

LottorNumber = []
for i in range(0,7):
    v = random.randint(1,45)
    LottorNumber.append(v)

print(LottorNumber)

## three
import random
print(random.sample(range(1,46),7))
