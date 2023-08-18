
op_type = \
    {
        "00000": "A",
        "00001": "A",
        "00010": "B",
        "00011": "C",
        "00100": "D",
        "00101": "D",
        "00110": "A",
        "00111": "C",
        "01000": "B",
        "01001": "B",
        "01010": "A",
        "01011": "A",
        "01100": "A",
        "01101": "C",
        "01110": "C",
        "01111": "E",
        "10000": "E",
        "10001": "E",
        "10010": "E",
        "10011": "F",
    }
opcodes = \
    {
        "00000": "add",
        "00001": "sub",
        "00010": "mov",
        "00011": "mov",
        "00100": "ld",
        "00101": "st",
        "00110": "mul",
        "00111": "div",
        "01000": "rs",
        "01001": "ls",
        "01010": "xor",
        "01011": "or",
        "01100": "and",
        "01101": "not",
        "01110": "cmp",
        "01111": "jmp",
        "10000": "jlt",
        "10001": "jgt",
        "10010": "je",
        "10011": "hlt",
    }
register_store = {
    "000": "0",
    "001": "0",
    "010": "0",
    "011": "0",
    "100": "0",
    "101": "0",
    "110": "0",
    "111": "0000000000000000"}

register_value= {
    "000": "0",
    "001": "0",
    "010": "0",
    "011": "0",
    "100": "0",
    "101": "0",
    "110": "0",
    "111": "0000000000000000"}

li=[]
anslist=[]
dic={}                 #number and instruction
dicvar={}               #variable store with number
def binaryToDecimal(n):
    return int(n,2)


def decimaltobinary(num):
    ne = int(num)
    bi = bin(ne).replace("0b", "")
    t = str(bi)
    le = 8 - len(t)
    for i in range(le):
        t = "0" + t
    return t


def add(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2)+int(reg3))
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def sub(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2)-int(reg3))
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def multiply(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2)*int(reg3))   
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def Exclusiveor(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2) ^ int(reg3))  
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def Or(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2) | int(reg3))
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def And(li):
    reg2=register_value[li[0][10:13]]
    reg3=register_value[li[0][13:16]]
    ans=str(int(reg2) & int(reg3))
    reg1 = li[0][7:10]
    register_value[reg1]=ans

def check():
    type=op_type[li[0][0:5]]
    inst=opcodes[li[0][0:5]]
    return type,inst

def final(typ,inst):
    if(typ=="A"):
        if(inst=="add"):
            add(li)
            register_value["111"]="0000000000000000"
        
        elif(inst=="sub"):
            sub(li)
            register_value["111"]="0000000000000000"
            

        elif(inst=="mul"):
            multiply(li)
            register_value["111"]="0000000000000000"
            
        
        elif(inst=="xor"):
            Exclusiveor(li)
            register_value["111"]="0000000000000000"
            

        elif(inst=="or"):
            Or(li)
            register_value["111"]="0000000000000000"
            
        
        elif(inst=="and"):
            And(li)
            register_value["111"]="0000000000000000"

    if (typ=="B"):
        if (inst=="mov"):
            imm_value=li[0][8:]
            reg=li[0][5:8]
            register_value[reg]=imm_value
            register_value["111"]="0000000000000000"

        elif(inst=="rs"):
            imm_value=str(li[0][8:])
            reg=li[0][5:8]
            sum=int(register_value[reg] >> (binaryToDecimal(imm_value)))
            register_value[reg]=sum
            register_value["111"]="0000000000000000"

        elif(inst=="ls"):
            imm_value=str(li[0][8:])
            reg=li[0][5:8]
            sum=int(register_value[reg] << (binaryToDecimal(imm_value)))
            register_value[reg]=sum
            register_value["111"]="0000000000000000"



    if(typ=="C"):
        if (inst=="div"):                                        #divsion of type C
            reg1=binaryToDecimal(register_value[li[0][10:13]])
            reg2=binaryToDecimal(register_value[li[0][13:]])
            quo=decimaltobinary(reg1//reg2)
            register_value["000"]=quo
            rem=decimaltobinary(reg1%reg2)
            register_value["001"]=rem
        elif(inst=="mov"):                                       #move register of type C
            reg2=register_value[li[0][13:]]
            register_value[li[0][10:13]]=reg2
            register_value["111"] = "0000000000000000"

        elif(inst=="not"):                                       #inverse of the type C
            reg2=int(register_value[li[0][13:]])
            bit=(~reg2)
            register_value[li[0][10:13]]=str(bit)
            register_value["111"] = "0000000000000000"

        elif(inst=="cmp"):                                        #compare pf type C
            reg1=register_value[li[0][10:13]]
            reg2=register_value[li[0][13:]]
            r1=binaryToDecimal(reg1)
            r2=binaryToDecimal(reg2)
            if (r1 > r2):
                register_value["111"] = "0000000000000010"
            elif (r1 < r2):
                register_value["111"] = "0000000000000100"
            else:
                register_value["111"] = "0000000000000001"
    if (typ=="D"):
        if (inst=="ld"):
            register_value[li[0][5:8]]=dicvar[li[0][8:]]
            register_value["111"] = "0000000000000000"

        elif(inst=="st"):
            reg1=register_value[li[0][5:8]]
            dicvar[li[0][8:]]=reg1
            register_value["111"] = "0000000000000000"

def main():
    i=0
    while True:
        l = input()
        if (l != "1001100000000000"):
            li.append(l)
            dic[i] = li[0]
            ty, ins = check()
            final(ty, ins)
            output()
            i += 1
        else:
            if (l =="1001100000000000"):
                li.append(l)
                dic[i] = "1001100000000000"
                output()
                i += 1
                break
            break

def output():
    temp = []
    for i in register_value.values():
        temp.append(i)
    anslist.append(temp)


def finaloutput():
    for i in anslist:
        for j in range(7):
            lt = len(i[j])
            c = 16 - lt
            t = c * "0"
            i[j] = t + i[j]
    tm=0
    for i in anslist:
        tm1 = decimaltobinary(tm)
        print(tm1,*i)
        tm=tm+1
    x=0
    for i in dic.values():
        print(i)
        x=x+1
    if(x<256):
        c = 256 - x
        for i in range(c):
            print("0000000000000000")





if __name__ == '__main__':
    main()
    finaloutput()