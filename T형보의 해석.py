condition=int(input('보의 양쪽에 슬래브가 있는 경우=1, 보의 한쪽에만 슬래브가 있는 경우=2'))
if condition==1:
    L=float(input('보 경간 L 입력(유효폭 b가 주어졌다면 1 입력)'))
    tf=float(input('플렌지 두께 tf 입력'))
    bw=float(input('보의 복부 폭 bw 입력'))
    slabdistance=float(input('양쪽 슬래브 중심간 거리 입력(유효폭 b가 주어졌다면 1 입력)'))
    list1=[L/4, 16*tf+bw, slabdistance]
    b=min(list1)
    print('L/4=%s/4, 16tf+bw=16 X %smm + %smm, slabdistance=%smm' %(L, tf, bw, slabdistance))
    
elif condition==2:
    L=float(input('보 경간 L 입력(유효폭 b가 주어졌다면 1 입력)'))
    tf=float(input('플렌지 두께 tf 입력'))
    bw=float(input('보의 복부 폭 bw 입력'))
    slabdistance=float(input('인접 보와의 내측거리 입력(유효폭 b가 주어졌다면 1 입력)'))
    list1=[L/12+bw, 6*tf+bw, slabdistance/2+bw]
    b=min(list1)
    print('L/12 + bw=%smm/12 + %smm=%smm, 6*tf+bw=%smm + %smm=%smm, slabdistance/2+bw=%smm/2 + %smm=%smm' %(L, bw, L/12+bw, tf, bw, 6*tf+bw, slabdistance, bw, slabdistance/2+bw))

b5=float(input('유효폭 b가 주어졌다면 여기에 입력, 아니면 0 입력'))
if b5!=0:
    b=b5

print('단근보라 가정하면')
print('유효 폭은',b,'mm 입니다.')

fck=int(input('fck 입력'))
fy=int(input('fy 입력'))
h=float(input('보의 높이 H'))   
d=float(input('철근부터 압축부까지의 보의 평균 높이 d 입력'))
dt=float(input('최외각 철근부터 압축부까지의 보의 최대 높이 dt 입력'))
numofsteel=int(input('철근의 개수 입력'))
D=int(input('철근의 호칭 입력'))
if D==22:
    A=387.1
if D==25:
    A=506.7
if D==29:
    A=642.4
As=A*numofsteel
As=round(As,4)

if fck<=28:
    B1=0.85
    print('B1=%s(fck=%s<=28MPa)' %(B1, fck))
elif fck>28:
    B1=0.85-(0.007)*(fck-28)
    if B1>=0.65:
        print('B1=0.85-(0.007)*(fck-28)=%s(fck=%s>28MPa)' %(B1, fck))
    elif B1<0.65:
        B1=0.65
        print('B1=0.85-(0.007)*(fck-28)=%s(fck=%s>28MPa)' %(B1, fck))

a=As*fy/(0.85*fck*b)
a=round(a,4)
Es=200000
Ey=fy/Es

print('a=Asfy/(0.85fckb)=%smm2 X %sMPa/(0.85 X %sMPa X %smm)=%smm)' %(As,fy, fck, b, a))






if a<tf:
    print('a=%smm<%smm' %(a, tf))
    Mn=As*fy*(d-a/2)/10**6
    Mn=round(Mn,4)
    print('Mn=As*fy*(d-a/2)/10**6=%smm2 X %sMpa X (%smm-%smm/2)/10**6=%skNm' %(As, fy, d, a, Mn))
    c=a/B1
    c=round(c,4)
    print('c=a/B1=%smm/%s=%smm' %(a, B1, c))
    Et=0.003*((dt-c)/c)
    Et=round(Et,4)
    print('Et=0.003*((dt-c)/c)=0.003 X (%smm-%smm)/(%smm)=%s' %(dt, c, c, Et))

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

    CalculatedStrength=Pi*As*fy*(d-a/2)/10**6
    CalculatedStrength=round(CalculatedStrength,4)
    print('ΦMn=%s X %skNm=%skNm' %(Pi, Mn, CalculatedStrength))

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

    yc= [((h-tf)+tf/2)*tf*b+((h-tf)**2)*bw/2]/(bw*(h-tf)+tf*b)
    Ixx = bw*(h-tf)*(yc-(h-tf)/2)**2 + (bw*(h-tf)**3)/12 + tf*b*((h-tf) + tf/2 - yc)**2 + (tf**3)*b/12

    lambda1=int(input('일반콘크리트=1, 경량콘크리트=2'))
    if lambda1==1:
        lambda1=1
    elif lambda1==2:
        lambda1=0.8
    fr=0.63*lambda1*fck**(1/2)
    fr=round(fr,4)
    Mcr=fr*Ixx*2/h/10**6
    Mcr=round(Mcr,4)
    print('fr=0.63람다 루트fck=0.63 X ',lambda1,' X 루트',fck,'MPa=',fr,'MPa')

    print('Mcr=frIg/Yt=',fr,'MPa X (',Ixx,'mm^4)/(',h,'mm/2)=',Mcr,'kNm')

    if CalculatedStrength<1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn<1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비에 못 미칩니다!***')
        print('로우<로우min')
    if CalculatedStrength>=1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비를 만족합니다!***')
        print('로우min<=로우')
    

    print('a는',a,'mm')
    print('c는',c,'mm')
    print('As는',As,'mm2')
    print('Et는',Et)
    print('Mn는',Mn,'kNm')
    print('Φ=',Pi)
    print('설계모멘트 ΦMn=',Pi*Mn,'kNm')
    print('fr',fr,'MPa')
    print('Mcr',Mcr,'kNm')
    print('1.2Mcr',round(1.2*Mcr,4),'kNm')


################################################################################################################################################################################################################################################


elif a>=tf:
    print('조금 복잡하겠습니다.')
    print('a=%smm>%smm=tf' %(a,tf))
    Cf=0.85*fck*(b-bw)*tf
    Asf=0.85*fck*(b-bw)*tf/fy
    Asf=round(Asf,4)
    print('Asf=0.85fck(b-bw)tf/fy=0.85 X %sMPa X (%smm-%smm) X %smm/%sMPa=%smm2' %(fck, b, bw, tf, fy, Asf))
    Mn1=Asf*fy*(d-tf/2)/10**6
    Mn1=round(Mn1,4)
    print('Mn1=Asffy(d-tf/2)/10^6=%smm2 X %sMpa X (%smm-%smm/2)/10^6=%skNm' %(Asf, fy, d, tf, Mn1))
    a=(As-Asf)*fy/(0.85*fck*bw)
    a=round(a,4)
    print('a=(As-Asf)fy/(0.85fckbw)=(%smm2-%smm2) X %sMPa/(0.85 X %sMPa X %smm)=%smm' %(As, Asf, fy, fck, bw, a))
    c=a/B1
    c=round(c,4)
    Et=0.003*((dt-c)/c)
    Et=round(Et, 4)

    Mn2=(As-Asf)*fy*(d-a/2)/10**6
    Mn2=round(Mn2,4)
    print('Mn2=(As-Asf)fy(d-a/2)/10**6=(%smm2-%smm2) X %sMPa X (%smm-%smm/2)/10^6=%skNm' %(As, Asf, fy, d, a, Mn2))

    Mn=Mn1+Mn2
    round(Mn, 4)
    print('Mn=Mn1+Mn2=%skNm+%skNm=%skNm' %(Mn1, Mn2, Mn))
    print('B1=',B1)
    print('c=a/B1=%smm/%s=%smm' %(a, B1, c))
    print('Et=0.003*((dt-c)/c)=0.003 X ((%smm-%smm)/%smm)=%s' %(dt, c, c, Et))
    
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

    yc= (((h-tf)+tf/2)*tf*b+((h-tf)**2)*bw/2)/(bw*(h-tf)+tf*b)
    Ixx = bw*(h-tf)*(yc-(h-tf)/2)**2 + (bw*(h-tf)**3)/12 + tf*b*((h-tf) + tf/2 - yc)**2 + (tf**3)*b/12

    lambda1=int(input('일반콘크리트=1, 경량콘크리트=2'))
    if lambda1==1:
        lambda1=1
    elif lambda1==2:
        lambda1=0.8
    fr=0.63*lambda1*fck**(1/2)
    fr=round(fr,4)
    Mcr=fr*Ixx*2/h/10**6
    Mcr=round(Mcr,4)
    CalculatedStrength=Pi*Mn
    CalculatedStrength=round(CalculatedStrength,4)
    print('ΦMn=%s X %skNm=%skNm' %(Pi, Mn, CalculatedStrength))
    print('fr=0.63람다 루트fck=0.63 X ',lambda1,' X 루트',fck,'MPa=',fr,'MPa')
    print('Mcr=frIg/Yt=',fr,'MPa X (',Ixx,'mm^4)/(',h,'mm/2)=',Mcr,'kNm')
    
    if CalculatedStrength<1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn<1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비에 못 미칩니다!***')
        print('로우<로우min')
    if CalculatedStrength>=1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비를 만족합니다!***')
        print('로우min<=로우')

    print('As는',As,'mm2')
    print('Asf는',Asf,'mm2')
    print('a는',a,'mm')
    print('c는',c,'mm')
    print('Et는',Et)
    print('Mn1는',Mn1,'kNm')
    print('Mn2는',Mn2,'kNm')
    print('Mn는',Mn,'kNm')
    print('Φ=',Pi)
    print('설계모멘트 ΦMn=',Pi*Mn,'kNm')
    print('fr',fr,'MPa')
    print('Mcr',Mcr,'kNm')
    print('1.2Mcr',round(1.2*Mcr,4),'kNm')