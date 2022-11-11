#print('kkkk\n ... bbbb\n ... aaaa')
#with open(r'./a.py',mode='rb')as f:
    #a=f.read()
    #print(a)

a=3.15
b='kaj'
c=6j
print(type(a))
print((int(a)))
print(complex(a))
print((str(c)))
#print(float(a))
print(len(b))



s1 = 72#去年的成绩
s2 = 85#今年的成绩
s3 = (s2-s1)/(s1*100)
print(f'小明从去年的{s1}分,到现在的{s2}分,提升了{s3*100:.2f}%')
print('小明从去年的{}分，到现在的{}分，提升了{:.2f}%'.format(s1,s2,s3*100))
print('小明从去年的%d分，到现在的%d分，提升了%f%%'%(s1,s2,s3*100))


classstudents=['刘语熙','曹永顺','李子良']
print(len(classstudents))
print(classstudents[0:-1])
classstudents.append('张兴慧')
print(classstudents)
classstudents.insert(3,'邓坤平')
print(classstudents)
classstudents.pop(3)
print(classstudents)
classstudents[3]='李俞鹏'
print(classstudents)
for classstudent in classstudents:
    cla=[11,['a','b','c'],3j]
    if 11 in cla:
        print(cla[1][1])
        if True:
            print(classstudent)
def els():
    s = int(input('birth: '))
    #birth = int(s)
    if s < 2000:
        print('00前')
    else:
        print('00后')
els()


aua=0
AG=[]
for a_ai in range(101):
    a_aiy=a_ai+a_ai
    a_ai+=1
    AG.append(a_aiy)
    au_a = aua + a_ai
    print(AG)
print(au_a)

OA=99
A=[]
s_ai=0
while OA>0:
    ss_aia=OA+s_ai
    OA=OA-2
    A.append(ss_aia)
print(A)


n = 0
m=[]
while n < 10:
    n = n + 1
    if n % 2 == 1: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    m.append(n)
print(m)


api={'白子画':['琴','剑','法力'],'杀阡陌':['笛子','长棍','法力'],'花千骨':['可爱','健康','善良']}
ppa={'长留':'修仙集团','七杀殿':'魔界','小骨的房子':'和平'}
print(api['花千骨'])
if ppa != api:
    api.update(**ppa)
for api_ai in api.items():
    print(api_ai)
api['糖宝']=['萌萌哒']
ppa.update({'仙界':['美丽','祥和','自然']})
print(ppa)
print(api)


def WAh():
    fja=set([1,2,3,1,2,3,3937,32,38.2,9j])
    fvas={'A':['l','b',9j],'AA':'好的吧','AAA':{'ah':9.856}}
    ven={'健康':'healthy'}
    fvas.update(**ven)
    for fva in fvas.items():
        print(fva)
        print(fja)
        fja.add(11)
    if 9j in fja and 9j in fvas:
        fvas['AA']='yes'
        print(fjas)
    if 2 in fja:
        fja.remove(2)
    print(fja)
WAh()
