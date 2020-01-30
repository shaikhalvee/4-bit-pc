s=['E_in', 'I_pc', 'L_pc', 'E_pc', 'L_mar', 'R_ram', 'W_ram', 'E_mdr',
   'L_mdr', 'L_ir', 'L_ir2', 'L_acc', 'E_acc', 'E_accm', 'E_accl', 'E_alu',
   'S_0', 'S_2', 'C_in', 'E_temp', 'L_temp', 'SH_1', 'SH_2', 'L_flag', 'E_flag',
   'E_flag2', 'L_flag1', 'E_sp', 'I_sp', 'D_sp', 'E_add', 'L_add', 'E_b', 'L_b', 'L_out', 'HLT',
   'L', 'R', 'C', 'Z', 'ADC', 'SBB']
s.reverse()


instructions=[]
f=open("input2.txt").readlines()
a=[]
for i in range(len(f)):
    if(f[i]=="\n"):
        if(len(a)==0):
            continue
        instructions.append(a)
        a=[]
    else:
        a.append(f[i])

for i in range(len(instructions)):
    ins=instructions[i]
    print(i,"==============")
    for j in range(len(ins)):
        p=ins[j].replace("\n","")
        print(p)

g=open("output.txt",'w')

outF=[open("output_"+str(i)+".bin",'w') for i in range(6)]

print("\n\n\n")
for i in range(len(instructions)):
    ins=instructions[i]
    print(i,"==============")
    for j in range(len(ins)):
        bits=[0 for i in range(max(len(s),48))]
        p=ins[j].replace("\n","").replace(" ","").split(",")
        for k in range(len(p)):
            bits[s.index(p[k])]=1

        
        ss=''
        for k in range(len(bits)):
            ss+=str(bits[k])
        
        hxs=hex(int(ss,2))
        print(hxs)
        g.write(hxs+'\n')

        sss=''
        for k in range(6):
            sss=''
            for m in range(8):
                sss+=str(bits[k*8+m])
            hxs=hex(int(sss,2))
            outF[6-k-1].write(hxs+'\n')
            
            

g.close()


for i in range(len(outF)):
    outF[i].close()

rom2file=open("rom2.bin",'w')

j=0
for i in range(len(instructions)):
    j+=len(instructions[i])
    print(i,j)
    rom2file.write(hex(int(j))+'\n')
rom2file.close()
    
