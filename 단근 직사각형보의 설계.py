import math

Pi=0
fy=0
fck=0
b=0
d=0
Mu=0

Pi=float(input('Pi'))
fck=float(input('fck'))
fy=float(input('fy'))
b=float(input('b'))
d=float(input('d'))
Mu=float(input('Mu'))*10**6

Q=(Pi*fy**2/(1.7*fck*b))
W=-(Pi*fy*d)
E=Mu
r1 = (-W + (W ** 2 - 4 * Q * E) ** 0.5) / (2 * Q)
r2 = (-W - (W ** 2 - 4 * Q * E) ** 0.5) / (2 * Q)
print(r1)
print(r2)
print('작은 값을 소수 첫째자리에서 올림 후')
print('(Pi*fy**2/(1.7*fck*b))As^2-(Pi*fy*d)As+Mu X 10^6=0')
print('(%s X %sMPa^2/(1.7 X %sMPa X %smm)) X As^2 - (%s X %sMPa X %smm)As + %skNm X 10^6=0' %(Pi, fy, fck, b, Pi, fy, d, Mu))
As=float(input('As=?'))

print('지름이 작은 철근부터 넣으세요~')
DSelection=int(input('D22=1, D25=2, D29=3'))
if DSelection==1:
    A=387.1
    NumofSteel=As/A
    print('철근의 개수=As/A=%smm2/%smm2' %(As,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('철근의 개수=',printNumofSteel,'개')

elif DSelection==2:
    A=506.7
    NumofSteel=As/A
    print('철근의 개수=As/A=%smm2/%smm2' %(As,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('철근의 개수=',printNumofSteel,'개')


elif DSelection==3:
    A=642.4
    NumofSteel=As/A
    print('철근의 개수=As/A=%smm2/%smm2' %(As,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('철근의 개수=',printNumofSteel,'개')