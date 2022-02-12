import math

fck=0
fy=0
b=0
h=0
d=0
dt=0
dp=0
B1=0
Mu=0
K=0
As=0
Asp=0
Pi=0
a=0
c=0
Et=0
D=0
DSelection=0
NumofSteel=0
Ey=0
Es=200000
Ey=fy/Es

Pi=0.85
fck=float(input('fck'))
fy=float(input('fy'))
b=float(input('b'))
h=float(input('h'))
d=float(input('d'))
dt=float(input('dt'))
dp=float(input('dp'))
Mu=float(input('Mu'))



print('압축철근이 항복하는 것을 가정')

if fck<=28:
    B1=0.85
elif fck>28:
    B1=0.85-(0.007)*(fck-28)
    if B1>=0.65:
        B1=B1
    elif B1<0.65:
        B1=0.65

print('B1=%s(fck=%s<=28MPa)' %(B1, fck))
print('As=k+Asp')



K=(B1*dp*0.85*fck*b)/((1-fy/600)*fy)
print('K=',K)

a=K*fy/(0.85*fck*b)
a=round(a,4)
print('a=',a)

c=a/B1
c=round(c,4)

print('c=',c)

Et=0.003*(dt/c-1)
Et=round(Et,4)
print('Et=',Et)

if fy>400:
        if Et>=2.5*Ey:
            Pi=0.85
            print('인장지배 단면입니다.')
        elif Et<=Ey:
            quest=input('띠철근=1 나선철근=2')
            if quest=='1':
                Pi=0.65
                print('압축지배 단면입니다.')
            elif quest=='2':
                Pi=0.70
                print('압축지배 단면입니다.')
        else:
            quest=input('띠철근=1 나선철근=2')
            if quest=='1':
                Pi=0.65+(Et-0.002)*(200/3)
                Pi=round(Pi,4)
                print('변화구간 단면입니다.')
            elif quest=='2':
                Pi=0.70+(Et-0.002)*(150/3)
                Pi=round(Pi,4)
                print('변화구간 단면입니다.')

if fy<=400:
    if Et>=0.005:
        Pi=0.85
        print('인장지배 단면입니다.')
    elif Et<=Ey:
        quest=input('띠철근=1 나선철근=2')
        if quest=='1':
            Pi=0.65
            print('압축지배 단면입니다.')
        elif quest=='2':
            Pi=0.70
            print('압축지배 단면입니다.')
    else:
        quest=input('띠철근=1 나선철근=2')
        if quest=='1':
            Pi=0.65+(Et-0.002)*(200/3)
            Pi=round(Pi,4)
            print('변화구간 단면입니다.')
        elif quest=='2':
            Pi=0.70+(Et-0.002)*(150/3)
            Pi=round(Pi,4)
            print('변화구간 단면입니다.')

if fy>400:
    if Et<2*Ey:
        print('***휨부재의 최소 허용변형률을 넘지 못했습니다!***')
elif fy<=400:
    if Et<0.004:
        print('***휨부재의 최소 허용변형률을 넘지 못했습니다!***')

print('항복되는 Asp 유도')

Asp=(Mu/Pi*10**6-K*fy*(d-K*fy/(1.7*fck*b)))/(fy*(d-dp))
Asp=round(Asp,4)
print('Asp=',Asp,'mm2')

As=K+Asp
print('As=%s' %As)

DSelection=int(input('D22=1, D25=2, D29=3'))
if DSelection==1:
    A=387.1
    NumofSteel=Asp/A
    print('압축 철근의 개수=Asp/A=%smm2/%smm2' %(Asp,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('압축 철근의 개수=',printNumofSteel,'개')

elif DSelection==2:
    A=506.7
    NumofSteel=Asp/A
    print('압축 철근의 개수=Asp/A=%smm2/%smm2' %(Asp,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('압축 철근의 개수=',printNumofSteel,'개')


elif DSelection==3:
    A=642.4
    NumofSteel=Asp/A
    print('압축 철근의 개수=Asp/A=%smm2/%smm2' %(Asp,A))
    printNumofSteel=math.ceil(NumofSteel)
    print('압축 철근의 개수=',printNumofSteel,'개')





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