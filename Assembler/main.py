def instr(inst):
    if (inst == "add"):
        Type = "A"
        opcode = "00000"
        return Type, opcode

    elif (inst == "sub"):
        Type = "A"
        opcode = "00001"
        return Type, opcode

    elif(inst=="mov"):
        if (l[2][0]=="$"):
            Type = "B"
            opcode = "00010"
            return Type, opcode

    if (inst=="mov"):
        Type = "C"
        opcode = "00011"
        return Type, opcode

    elif (inst == "ld"):
        Type = "D"
        opcode = "00100"
        return Type, opcode

    elif (inst == "st"):
        Type = "D"
        opcode = "00101"
        return Type, opcode

    elif (inst == "mul"):
        Type = "A"
        opcode = "00110"
        return Type, opcode

    elif (inst == "div"):
        Type = "C"
        opcode = "00111"
        return Type, opcode

    elif (inst == "rs"):
        Type = "B"
        opcode = "01000"
        return Type, opcode

    elif (inst == "ls"):
        Type = "B"
        opcode = "01001"
        return Type, opcode

    elif (inst == "xor"):
        Type = "A"
        opcode = "01010"
        return Type, opcode

    elif (inst == "or"):
        Type = "A"
        opcode = "01011"
        return Type, opcode

    elif (inst == "and"):
        Type = "A"
        opcode = "01100"
        return Type, opcode

    elif (inst == "not"):
        Type = "C"
        opcode = "01101"
        return Type, opcode

    elif (inst == "cmp"):
        Type = "C"
        opcode = "01110"
        return Type, opcode

    elif (inst == "jmp"):
        Type = "E"
        opcode = "01111"
        return Type, opcode

    elif (inst == "jlt"):
        Type = "E"
        opcode = "10000"
        return Type, opcode

    elif (inst == "jgt"):
        Type = "E"
        opcode = "10001"
        return Type, opcode

    elif (inst == "je"):
        Type = "E"
        opcode = "10010"
        return Type, opcode

    elif (inst == "hlt"):
        Type = "F"
        opcode = "10011"
        return Type, opcode
    else:
        return "false"," "


def register(reg):
    if (reg == "R0"):
        return "000"
    elif (reg == "R1"):
        return "001"
    elif (reg == "R2"):
        return "010"
    elif (reg == "R3"):
        return "011"
    elif (reg == "R4"):
        return "100"
    elif (reg == "R5"):
        return "101"
    elif (reg == "R6"):
        return "110"
    elif (reg == "FLAGS"):
        return "111"
    else:
        return "false"


def dectobin(num):
    ne = int(num)
    bi = bin(ne).replace("0b", "")
    t = str(bi)
    le = 8 - len(t)
    for i in range(le):
        t = "0" + t
    return t


def instruction(typ, op):
    if (typ == "A"):
        unused = "00"
        r = register(l[1])
        r1 = register(l[2])
        r2 = register(l[3])
        if(r!="false" and r1!="fasle" and r2!="false"):
            res = op + unused + r + r1 + r2
            return res
        return "false"
    elif (typ == "B"):
        r = register(l[1])
        if(int(l[2][1:])<255 and int(l[2][1:])>0):
            im = dectobin(l[2][1:])
        else:
            im="false"
        if (r!="false" and im!="false"):
            res = op + r + im
            return (res)
        if (r=="false" or im=="false"):
            return "false"
    elif (typ == "C"):
        unused = "00000"
        r = register(l[1])
        r1 = register(l[2])
        if (r!="false" and r1!="false"):
            res =  (op + unused + r + r1)
            return (res)
        if (r=="false" or r1=="false"):
            return "false"
    elif (typ == "D"):
        r = register(l[1])
        bii = dectobin(var+1)
        if (r=="false"):
            return "false"
        elif (r!="false"):
            res = op + r + bii
            return res
    elif (typ == "E"):
        unused = "000"
        bii = dectobin(var )
        res = op + unused + bii
        return res
    elif (typ == "F"):
        unused = "00000000000"
        res = op + unused
        return res
    else:
        return "false"

def respr(x):
        for i in range(len(x)):
            print(x[i])

if __name__ == '__main__':
    li = []
    var = 0
    line=0
    temp=[]
    label=[]
    while (True):
        l = list(map(str, input().split()))
        if (l[0][-1]==":"):
            label = l.copy()
            l.remove(label[0])
        if(l[0]=="var"):
            temp.append(l[0])
            temp.append(l[1])
        else:
            en = l[0]
            var = var + 1
            tye, ope = instr(l[0])
            if (tye == "false"):
                li.append("Instruction is invalid in line ")
                break
            if (en == "hlt"):
                var = var + 1
                result = instruction(tye, ope)
                li.append(result)
                break
            result = instruction(tye, ope)
            if (result == "false"):
                if (tye == "A"):
                    li.append("Register is invalid in line " + str(line))
                elif (tye == "B"):
                    if (int(l[2][1:]) > 255 or int(l[2][1:]) < 0):
                        li.append("Valuse should between 0 to 255 in line " + str(line))
                    else:
                        li.append("Register is invalid in line " + str(line))
                elif (tye == "C" or tye == "D"):
                    li.append("Register is invalid in line " + str(line))
            if (result != "false"):
                li.append(result)


    respr(li)
    

