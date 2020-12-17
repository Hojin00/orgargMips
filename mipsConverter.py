#authors Heitor Feijo Kunrath e Hojin Ryu 류호진


file=input("qual é o nome da file que deseja abrir com .asm?")
b=input("digite 1 se deseja converter de asm para hex e 2 se deseja converter de hex para asm")
f=open(file, "r")

def oitoBits(a):
    if len(a)<10:
        a= "0x"+a[2:].zfill(8)

        return a
    else:
        return a
if b=="1":    
    DicOpcode={  "div": "000000" ,"nor": "000000" , "ori": "001101",
           "sll": "000000" , "slti": "001010" , "beq": "000100",
           "blez": "000110", "jal":"000011", "lw": "100011", "jr":"000000"}
    output="" # \n nova linha
    DicFunc = { "jr" : "001000" , "div" : "011010",
               "nor" : "100111", "sll" : "000000"}
    a= f.readlines()
    J=["jal"]
    R=["jr","div","nor","sll"]
    I=["lw","beq","blez","ori","slti"]
    for i in a:
        #RI= False # diz se e do tipo I ou R 
        opResto=i.split()
        opcode= opResto[0]
        resto=opResto[1]
        listResto=resto.split(",")
        if opcode in J: 
            resto= resto[2:]
           
            
            aux2=str(bin(int(resto,16)))[2:]
            
            if len(aux2)<32:
                aux2= aux2.zfill(32)
                aux2=aux2[4:]
                aux2=aux2[:-2]
            aux2=str(aux2)
            output+= oitoBits(hex(int(DicOpcode[opcode]+aux2,2)))+"\n"
            
            
        elif opcode in R:
            
            if opcode=="jr":
                opBin=DicOpcode[opcode]
                func=DicFunc[opcode]
                rs= str(bin(int(resto[1:])))[2:]
                rt="00000"
                rd="00000"
                output+=oitoBits(hex(int(opBin+rs+rt+rd+"00000"+func,2)))+"\n"
            elif opcode=="div":
                opBin=DicOpcode[opcode]
                func=DicFunc[opcode]
                rd="00000"
                inpu=resto.split(",")
                rs=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                output+=oitoBits(hex(int(opBin+rs+rt+rd+"00000"+func,2)))+"\n"
            elif opcode=="nor":
                opBin=DicOpcode[opcode]
                func=DicFunc[opcode]
                inpu=resto.split(",")
                rd=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rs=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[2][1:])))[2:].zfill(5)
                output+=oitoBits(hex(int(opBin+rs+rt+rd+"00000"+func,2)))+"\n"
            elif opcode=="sll":
                opBin=DicOpcode[opcode]
                func=DicFunc[opcode]
                inpu=resto.split(",")
                rs="00000"
                rd=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                shamt=str(bin(int(inpu[2][2:],16)))[2:].zfill(5)
                output+=oitoBits(hex(int(opBin+rs+rt+rd+shamt+func,2)))+"\n"
            
        else:# I
            if opcode=="lw":
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                rt=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rs=str(bin(int(inpu[1][12:-1])))[2:].zfill(5)
                NotImm=inpu[1][2:-4].zfill(32)
                imm= str(bin(int(NotImm,16)))[2:].zfill(32)[16:]
                output+=oitoBits(hex(int(opBin+rs+rt+imm,2)))+"\n"
                
            elif opcode=="beq":
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                rs=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                NotImm=inpu[2][2:].zfill(32)
                imm= str(bin(int(NotImm,16)))[2:].zfill(32)[16:]
                output+=oitoBits(hex(int(opBin+rs+rt+imm,2)))+"\n"
                
            elif opcode=="blez":
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                rs=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                rt="00000"
                NotImm=inpu[1][2:].zfill(32)
                imm= str(bin(int(NotImm,16)))[2:].zfill(32)[16:]
                output+=oitoBits(hex(int(opBin+rs+rt+imm,2)))+"\n"
            elif opcode=="ori":
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                rs=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                NotImm=inpu[2][2:].zfill(32)
                imm= str(bin(int(NotImm,16)))[2:].zfill(32)[16:]
                output+=oitoBits(hex(int(opBin+rs+rt+imm,2)))+"\n"
            elif opcode=="slti":
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                opBin=DicOpcode[opcode]
                inpu=resto.split(",")
                rs=str(bin(int(inpu[1][1:])))[2:].zfill(5)
                rt=str(bin(int(inpu[0][1:])))[2:].zfill(5)
                NotImm=inpu[2][2:].zfill(32)
                imm= str(bin(int(NotImm,16)))[2:].zfill(32)[16:]
                output+=oitoBits(hex(int(opBin+rs+rt+imm,2)))+"\n"
    
    print(output)
    fn= open("AsmToHexHeitorHojin.asm","w+")
    fn.close()
    fn= open("AsmToHexHeitorHojin.asm","a+")
    fn.write(output)
    print("a file 'AsmToHexHeitorHojin.asm' foi criado na pasta do programa contendo o codigo acima")
    fn.close()

    #temos que escrever aqui a file 
if b=="2":    
    DicFunc = { "001000" : "jr" , "011010" : "div", "100111" : "nor", "000000" : "sll"}
    
    
    decodific = open(file, "r")
    decodHex = decodific.readlines()
    
    
    DicTipoI = {"100011": "lw", "000100": "beq",
               "000110": "blez", "001101": "ori", "001010": "slti"  }
    
    DicTipoJ={  "000011":"jal" }
    
    hexToBinario = []
    todasInstrucoes = ""
    
    for i in decodHex: # Convertendo hexadecimal pro binario e guardando no hexToBinario array.
        ini_hex = i
        ini_hex = ini_hex[2:]
        hex_Binario = ''
        hex_Binario = str(bin(int(ini_hex,16)))[2:].zfill(32)
        hexToBinario.append(hex_Binario)
    
    for opcodes in hexToBinario:
    
        if opcodes[:6] == '000000': #aqui comeca instrucoes tipo-R.
    
    
            rs = ""
            rt = ""
            rd = ""
    
            if int(opcodes[6:11],2) > 0:
                rs = "$" + str(int(opcodes[6:11],2))
            if int(opcodes[11:16],2) > 0:
                rt = "$" + str(int(opcodes[11:16],2))
            if int(opcodes[16:21],2) > 0:
                rd = "$" + str(int(opcodes[16:21],2))
    
            instrucoes = DicFunc[opcodes[-6:]] + " " + rs + " " + rt + " " + rd
    
    
            if DicFunc[opcodes[-6:]] == 'jr' or DicFunc[opcodes[-6:]] == 'div': # instrucoes jr, div
                instrucoes = DicFunc[opcodes[-6:]] + " " + rs + " " + rt + " " + rd
    
                todasInstrucoes += instrucoes + "\n"
    
            if DicFunc[opcodes[-6:]] == 'sll': # sll
    
                shamt = "0x" + str(hex(int(opcodes[21:26],2)))[2:].zfill(8)
    
                instrucoes = DicFunc[opcodes[-6:]] + " " + rd + " " + rt + " " + shamt
    
                todasInstrucoes += instrucoes + "\n"
    
            if DicFunc[opcodes[-6:]] == 'nor': # nor
                instrucoes = DicFunc[opcodes[-6:]] + " " + rd + " " + rs + " " + rt
    
                todasInstrucoes += instrucoes + "\n"
    
    
    
    
    
        if not opcodes[:6] == '000011': #aqui comeca instrucoes tipo-I.
    
    
            for i in DicTipoI:
                if i == opcodes[:6]:
    
                    rs = ""
                    rt = ""
                    imm = ""
    
                    if int(opcodes[6:11],2) > 0:
                        rs = "$" + str(int(opcodes[6:11],2))
                    if int(opcodes[11:16],2) > 0:
                        rt = "$" + str(int(opcodes[11:16],2))
    
                    imm = "0x" + str(hex(int(opcodes[-16:],2)))[2:].zfill(8)
    
    
    
                    if DicTipoI[opcodes[:6]] == DicTipoI["100011"]: # para a instrucao "lw"
    
                        instrucoes = DicTipoI[opcodes[:6]] + " " + rt + " " + imm + "(" + rs + ")"
    
                        todasInstrucoes += instrucoes + "\n"
    
                    if DicTipoI[opcodes[:6]] == DicTipoI["000100"] or DicTipoI[opcodes[:6]] == DicTipoI["001101"]: #beq, ori
    
                        instrucoes = DicTipoI[opcodes[:6]] + " " + rs + " " + rt + " " + imm
    
                        todasInstrucoes += instrucoes + "\n"
    
                    if DicTipoI[opcodes[:6]] == DicTipoI["001010"]:# slti
    
                        instrucoes = DicTipoI[opcodes[:6]] + " " + rt + " " + rs + " " + imm
    
                        todasInstrucoes += instrucoes + "\n"
    
    
                    if DicTipoI[opcodes[:6]] == DicTipoI["000110"]: #blez
    
                        instrucoes = DicTipoI[opcodes[:6]] + " " + rs + " " + imm
    
                        todasInstrucoes += instrucoes + "\n"
    
        else: # tipo-J (jal).
            endereco = "0000" + opcodes[-26:] + "00"
            endereco = "0x" + str(hex(int(endereco,2)))[2:].zfill(8)
    
            instrucoes = DicTipoJ[opcodes[:6]] + " " + endereco
            todasInstrucoes += instrucoes + "\n"
    
    print(todasInstrucoes)             
    fn= open("HexToAsmHeitorHojin.asm","w+")
    fn.close()
    fn= open("HexToAsmHeitorHojin.asm","a+")
    fn.write(todasInstrucoes)
    print("a file 'HexToAsmHeitorHojin.asm' foi criado na pasta do programa contendo o codigo acima")
    fn.close()