out=[]
with open('xlxd_exam.txt') as fi:
    with open('result.txt') as fj:
        for i in range(1001):
            badcar=False
            while(True):
                line1=fi.readline()
                line2=fj.readline()
                if line1=='':
                    if badcar==True:
                        label=1
                    else:
                        label=0
                    out.append(str(label)+'\n')
                    break
                #print(line1)
                #print(line2)
                if line1 =='car_'+str(i)+'\n':
                    print(line1)
                    if i ==0:
                        pass
                    else:
                        if badcar==True:
                            label=1
                        else:
                            label=0
                        out.append(str(label)+'\n')
                    break
                elif line2=='__label__1\n':
                    print('true')
                    badcar=True
                elif line2=='__label__0\n':
                    print('pass')
                    pass
                else:
                    print(line2)

with open('car_out.txt','w') as f:
    f.writelines(out)