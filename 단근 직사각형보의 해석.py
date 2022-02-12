fck=float(input('fck 입력'))
fy=float(input('fy 입력'))
b=float(input('b 입력'))
h=float(input('h 입력'))
dt=float(input('dt 입력'))
D=float(input('철근 호칭'))
NumofSteel=float(input('철근의 개수'))

if fck == 27 and fy == 400:
    pmax=0.0209
    pmin=0.0048
if D==22:
    A=387.1
if D==25:
    A=506.7
if D==29:
    A=642.4
As=NumofSteel*A

if fck<=28:
    B1=0.85
    print('B1=%s(fck=%s<=28MPa)' %(B1, fck))
elif fck>28:
    B1=0.85-(0.007)*(fck-28)
    if B1>=0.65:
        B1=B1
        print('B1=0.85-(0.007)*(fck-28)=%s(fck=%s>28MPa)' %(B1, fck))
    elif B1<0.65:
        B1=0.65
        print('B1=0.85-(0.007)*(fck-28)=%s(fck=%s>28MPa)' %(B1, fck))

a=As*fy/(0.85*fck*b)
a=round(a,4)
Mn=As*fy*(dt-a/2)/10**6
Mn=round(Mn,4)
c=a/B1
c=round(c,4)
Et=0.003*(dt-c)/c
Et=round(Et,4)
Es=200000
Ey=fy/Es
print('fck=',fck,'MPa')
print('fy=',fy,'MPa')
print('a=Asfy/(0.85fckb)=',As,'mm2 X',fy,'MPa/(0.85 X',fck,'MPa X',b,'mm)=',a,'mm')
print('Et=0.003(dt-c)/(c)=0.003(',dt,'mm-',c,'mm)/(',c,'mm)=',Et)


if fy>400:
    if Et>=2.5*Ey:
        Pi=0.85
        print('인장지배 단면입니다.')
        print('Φ=',Pi)
    elif Et<=Ey:
        quest=input('띠철근=1 나선철근=2')
        if quest=='1':
            Pi=0.65
            print('압축지배 단면입니다.')
            print('Φ=',Pi)
        elif quest=='2':
            Pi=0.70
            print('압축지배 단면입니다.')
            print('Φ=',Pi)
    else:
        quest=input('띠철근=1 나선철근=2')
        if quest=='1':
            Pi=0.65+(Et-0.002)*(200/3)
            Pi=round(Pi,4)
            print('변화구간 단면입니다.')
            print('Φ=',Pi)
        elif quest=='2':
            Pi=0.70+(Et-0.002)*(150/3)
            Pi=round(Pi,4)
            print('변화구간 단면입니다.')
            print('Φ=',Pi)
                

    if fy<=400:
        if Et>=0.005:
            Pi=0.85
            print('인장지배 단면입니다.')
            print('Φ=',Pi)
        elif Et<=Ey:
            quest=input('띠철근=1 나선철근=2')
            if quest=='1':
                Pi=0.65
                print('압축지배 단면입니다.')
                print('Φ=',Pi)
            elif quest=='2':
                Pi=0.70
                print('압축지배 단면입니다.')
                print('Φ=',Pi)
        else:
            quest=input('띠철근=1 나선철근=2')
            if quest=='1':
                Pi=0.65+(Et-0.002)*(200/3)
                Pi=round(Pi,4)
                print('변화구간 단면입니다.')
                print('Φ=',Pi)
            elif quest=='2':
                Pi=0.70+(Et-0.002)*(150/3)
                Pi=round(Pi,4)
                print('변화구간 단면입니다.')
                print('Φ=',Pi)



if fy>400:
    if Et<2*Ey:
        print('***휨부재의 최소 허용변형률을 넘지 못했습니다!***')
        print('로우>로우max')
    elif Et>=2*Ey:
        print('Et=',Et,'>=',2*Ey,'이므로 로우<=로우max')
elif fy<=400:
    if Et<0.004:
        print('***휨부재의 최소 허용변형률을 넘지 못했습니다!***')
        print('로우>로우max')
    elif Et>=0.004:
        print('Et=',Et,'>=0.004이므로 로우<=로우max')
CalculatedStrength=Pi*Mn
CalculatedStrength=round(CalculatedStrength,4)

z=b/6*h**2
lambda1=int(input('일반콘크리트=1, 경량콘크리트=2'))
if lambda1==1:
    lambda1=1
elif lambda1==2:
    lambda1=0.8
fr=0.63*lambda1*fck**(1/2)
fr=round(fr,4)
Mcr=fr*z/10**6
Mcr=round(Mcr,4)



print('Mn=Asfy(d-a/2)=',As,'mm2 X',fy,'MPa X (',dt,'mm-',a,'mm/2) X 10^-6=',Mn,'kNm')
print('ΦMn=',Pi,'X',Mn,'kNm=',CalculatedStrength,'kNm')
print('Et=0.003(dt-c)/(c)=0.003(%s-%s)/(%s)=%s' %(dt, c, c,Et))
print('fr=0.63람다 루트fck=0.63 X ',lambda1,' X 루트',fck,'MPa=',fr,'MPa')
print('Mcr=frIg/Yt=frbh^2/6=',fr,'MPa X (',b,'mm/6) X (',h,'mm)^2 X 10^-6=',Mcr,'kNm')
print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
if CalculatedStrength<1.2*Mcr:
    print(CalculatedStrength,'kNm=ΦMn<1.2Mcr=',round(1.2*Mcr,4),'kNm')
    print('***최소 철근비에 못 미칩니다!***')
    print('로우<로우min')
if CalculatedStrength>=1.2*Mcr:
    print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
    print('***최소 철근비를 만족합니다!***')
    print('로우min<=로우')



#print('b=',b)
#print('dt=',dt)
#print('철근 호칭=',D)
#print('철근의 개수=',NumofSteel)
#print('pmax=',pmax)
#print('pmin=',pmin)
#print('As=',As)
#print('B1=',B1)
#print('a=',a)
#print('c=',c)
#print('Mn=',Mn,'kNm')
#print('Et=',Et) 
#print('2.5Ey=',2.5*Ey) 
#print('Φ=',Pi)
#print('설계모멘트 ΦMn=',CalculatedStrength,'kNm')
#print('lambda1=',lambda1)
#print('fr=',fr)
#print('Mcr=',Mcr)
#print('1.2Mcr=',1.2*Mcr)
#print('z=',z)





