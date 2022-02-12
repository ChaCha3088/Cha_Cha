fck=0
fy=0
h=0
b=0
d=0
dt=0
ComAsp=0
TenAsp=0
dp=0
a=0
c=0
NumofCSteel=0
NumofTSteel=0
ComD=0
TenD=0
ComA=0
TenA=0
TenAs=0
Esp=0
Mn=0
Et=0
Es=0
Ey=0
Pi=0
quest=0
CalculatedStrength=0
z=0
lambda1=0
fr=0
Mcr=0
fsp=0
Cc=0
Cs=0
B1=0

fck=int(input('fck 입력'))
fy=int(input('fy 입력'))
b=float(input('b 입력'))
d=float(input('d 입력'))
h=float(input('H 입력'))
dt=float(input('최외각 철근 dt 입력'))
dp=float(input('dp 입력'))
NumofCSteel=int(input('압축 철근 개수 입력'))
ComD=int(input('압축 철근 호칭'))
NumofTSteel=int(input('인장 철근 개수 입력'))
TenD=int(input('인장 철근 호칭'))

print('fck=%sMPa, fy=%sMPa' %(fck, fy))





if ComD==22:
    ComA=387.1
if ComD==25:
    ComA=506.7
if ComD==29:
    ComA=642.4
if TenD==22:
    TenA=387.1
if TenD==25:
    TenA=506.7
if TenD==29:
    TenA=642.4

TenAs=NumofTSteel*TenA
ComAsp=NumofCSteel*ComA
TenAsp=NumofCSteel*TenA
Es=200000
Ey=fy/Es
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


print('압축 철근이 항복함을 가정.')
a=((TenAs-TenAsp)*fy)/(0.85*fck*b)
a=round(a,4)
c=a/B1
c=round(c,4)
Esp=((c-dp)/c)*0.003
Esp=round(Esp,4)
Et=0.003*((dt-c)/c)
Et=round(Et,4)
print('a=',a,'mm')
print('c=',c,'mm')
print('Esp=',Esp)


if Esp<Ey:
    print('a=(As-Asp)fy/(0.85fckb)=(%smm2-%smm2) X %sMPa/(0.85 X %sMPa X %smm)=%smm' %(TenAs, TenAsp, fy, fck, b, a))
    print('c=a/B1=%smm/%s=%smm' %(a, B1, c))
    print('Esp=0.003(c-dp)/(c)=0.003(%smm-%smm)/(%smm)=%s<Ey=%s' %(c, dp, c, Esp, Ey))
    print('***압축 철근이 항복하지 않았습니다.***')
    print('(0.85fckb)a^2+(0.003EsAsp-Asfy)a-(0.003EsAspB1dp)=0')
    print('(0.85 X %s X %s) X a^2+(0.003 X %s X %s-%s X %s)a-(0.003 X %s X %s X %s X %s)=0' %(fck, b, Es, TenAsp, TenAs, fy, Es, TenAsp, B1, dp))
    


    Q=0.85*fck*b
    W=0.003*Es*ComAsp-TenAs*fy
    E=-(0.003*Es*ComAsp*B1*dp)
    r1 = (-W + (W ** 2 - 4 * Q * E) ** 0.5) / (2 * Q)
    r2 = (-W - (W ** 2 - 4 * Q * E) ** 0.5) / (2 * Q)
    print(r1)
    print(r2)
    if r1>0:
        a=r1
        a=round(a,4)
    if r2>0:
        a=r2
        a=round(a,4)
    c=a/B1
    c=round(c,4)
    print('a=%smm' %(a))
    print('c=a/B1=%smm/%s=%smm' %(a,B1, c))
    Esp=0.003*(c-dp)/(c)
    Esp=round(Esp,4)
    print('Esp=0.003(c-dp)/(c)=0.003 X (%smm - %smm)/(%smm)=%s' %(c, dp, c, Esp))
    fsp=Es*Esp
    print('fsp=EsEsp=%s X %s=%sMPa' %(Es, Esp, fsp))
    Cc=0.85*fck*a*b
    Cs=ComAsp*fsp
    Et=0.003*((dt-c)/c)
    Et=round(Et, 4)
    Mn=(Cc*(d-a/2)+Cs*(d-dp))/10**6
    Mn=round(Mn,4)
    print('Mn=Cc(d-a/2)+Cs(d-dp)=0.85fckab(d-a/2) + Aspfsp(d-dp)')
    print('=0.85 X %sMPa X %smm X %smm X (%smm-%smm/2) X 10^-6+%smm2 X %sMpa X (%smm-%smm) X 10^-6' %(fck, a, b, d, a, TenAsp, fsp, d, dp))
    print('=%skNm' %(Mn))
    print('Et=0.003(dt-c)/(c)=0.003(%smm-%smm)/(%smm)=%s' %(dt, c, c, Et))
    

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

    print('Φ=%s' %(Pi))
    print('ΦMn=%s X %skNm=%skNm' %(Pi,Mn,CalculatedStrength))
    print('fr=0.63람다 루트fck=0.63 X ',lambda1,' X 루트',fck,'MPa=',fr,'MPa')
    print('Mcr=frIg/Yt=frbh^2/6=',fr,'MPa X (',b,'mm/6) X (',h,'mm)^2 X 10^-6=',Mcr,'kNm')

    if CalculatedStrength<1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn<1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비에 못 미칩니다!***')
        print('로우<로우min')
    if CalculatedStrength>=1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비를 만족합니다!***')
        print('로우min<=로우')

    

    



    print('fck=',fck,'Mpa')
    print('fy=',fy,'MPa')
    print('h=',h,'mm')
    print('b=',b,'mm')
    print('d=',d,'mm')
    print('dt=',dt,'mm')
    print('dp=',dp,'mm')
    print('압축 철근의 개수=',NumofCSteel,'개')
    print('압축 철근 호칭=D',ComD)
    print('인장 철근의 개수=',NumofTSteel,'개')
    print('인장 철근 호칭=D',TenD)
    
    #print('pmax=',pmax)
    #print('pmin=',pmin)
    print('a=',a,'mm')
    print('c=',c,'mm')
    print('Esp=',Esp)
    print('fsp=',fsp)
    print('Mn=',Mn,'kNm')
    print('Et=',Et) 
    print('2.5Ey=',2.5*Ey)
    print('Φ=',Pi)
    print('설계모멘트 ΦMn=',CalculatedStrength,'kNm')
    print('lambda1=',lambda1)
    print('fr=',fr,'MPa')
    print('Mcr=',Mcr,'kNm')
    print('1.2Mcr=',round(1.2*Mcr,4),'kNm')


    


########################################################################################################################################################################################

elif Esp>=Ey:
    print('a=(As-Asp)fy/(0.85fckb)=(%smm2-%smm2) X %sMPa/(0.85 X %sMPa X %smm)=%smm' %(TenAs, TenAsp, fy, fck, b, a))
    print('c=a/B1=%smm/%s=%smm' %(a, B1, c))
    print('Esp=0.003(c-dp)/(c)=0.003(%s-%s)/(%s)=%s>=Ey=0.002' %(c, dp, c, Esp))
    print('***압축 철근이 항복하였습니다.***')
        
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

    print('Et=0.003(dt-c)/(c)=0.003(%s-%s)/(%s)=%s' %(dt, c, c, Et))


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

    

    Mn=ComAsp*fy*(d-dp)/10**6+(TenAs-TenAsp)*fy*(d-a/2)/10**6
    Mn=round(Mn,4)
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

    print('Mn=Aspfy(d-dp)+(As-Asp)fy(d-a/2)=%smm2 X %sMPa X (%smm-%smm) X 10^-6 + (%smm2-%smm2) X %s (%smm-%smm/2) X 10^-6=%skNm' %(ComAsp, fy, d, dp, TenAs, ComAsp, fy, d, a, Mn))
    print('ΦMn=',Pi,'X',Mn,'kNm=',CalculatedStrength,'kNm')
    print('fr=0.63람다 루트fck=0.63 X ',lambda1,' X 루트',fck,'MPa=',fr,'MPa')
    print('Mcr=frIg/Yt=frbh^2/6=',fr,'MPa X (',b,'mm/6) X (',h,'mm)^2 X 10^-6=',Mcr,'kNm')

    if CalculatedStrength<1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn<1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비에 못 미칩니다!***')
        print('로우<로우min')
    if CalculatedStrength>=1.2*Mcr:
        print(CalculatedStrength,'kNm=ΦMn>=1.2Mcr=',round(1.2*Mcr,4),'kNm')
        print('***최소 철근비를 만족합니다!***')
        print('로우min<=로우')

    

    



    print('fck=',fck,'Mpa')
    print('fy=',fy,'MPa')
    print('h=',h,'mm')
    print('b=',b,'mm')
    print('d=',d,'mm')
    print('dt=',dt,'mm')
    print('dp=',dp,'mm')
    print('압축 철근의 개수=',NumofCSteel,'개')
    print('압축 철근 호칭=D',ComD)
    print('인장 철근의 개수=',NumofTSteel,'개')
    print('인장 철근 호칭=D',TenD)
    #print('pmax=',pmax)
    #print('pmin=',pmin)
    print('a=',a,'mm')
    print('c=',c,'mm')
    print('Esp=',Esp)
    print('Mn=',Mn,'kNm')
    print('Et=',Et) 
    print('2.5Ey=',2.5*Ey) 
    print('Φ=',Pi)
    print('설계모멘트 ΦMn=',CalculatedStrength,'kNm')
    print('lambda1=',lambda1)
    print('fr=',fr,'MPa')
    print('Mcr=',Mcr,'kNm')
    print('1.2Mcr=',round(1.2*Mcr,4),'kNm')














