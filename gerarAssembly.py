def gerarAssembly(tokens):
    tokens = [str(t) for t in tokens]
    
    codigo = []
    
    variaveis = set()
    for t in tokens:
        if t.isalpha() and t.isupper() and t != "RES":
            variaveis.add(t)
            
    codigo.append(".data")
    codigo.append("RES_ARRAY: .space 8000")
    for v in variaveis:
        codigo.append(f"{v}: .double 0.0")
        
    codigo.append(".text")
    codigo.append(".global _start")
    codigo.append("_start:\n")
    codigo.append("    LDR R10, =RES_ARRAY\n")
    
    depth = 0
    label_cnt = 0
    
    for i, token in enumerate(tokens):
        if token == "(":
            depth += 1
            
        elif token == ")":
            depth -= 1
            if depth == 0:
                codigo += [
                    "    VPOP {D0}",
                    "    VSTR.F64 D0, [R10]",
                    "    ADD R10, R10, #8\n"
                ]
                
        elif token == "+":
            codigo += [
                "    VPOP {D1}",
                "    VPOP {D0}",
                "    VADD.F64 D0, D0, D1",
                "    VPUSH {D0}\n"
            ]
            
        elif token == "-":
            codigo += [
                "    VPOP {D1}",
                "    VPOP {D0}",
                "    VSUB.F64 D0, D0, D1",
                "    VPUSH {D0}\n"
            ]
            
        elif token == "*":
            codigo += [
                "    VPOP {D1}",
                "    VPOP {D0}",
                "    VMUL.F64 D0, D0, D1",
                "    VPUSH {D0}\n"
            ]
            
        elif token == "/":
            codigo += [
                "    VPOP {D1}",
                "    VPOP {D0}",
                "    VDIV.F64 D0, D0, D1",
                "    VPUSH {D0}\n"
            ]
            
        elif token == "//":
            codigo += [
                "    VPOP {D1}",             
                "    VPOP {D0}",            
                "    VDIV.F64 D0, D0, D1",   
                "    VCVT.S32.F64 S0, D0",   
                "    VCVT.F64.S32 D0, S0",   
                "    VPUSH {D0}\n"
            ]
            
        elif token == "%":
            codigo += [
                "    VPOP {D1}",          
                "    VPOP {D0}",             
                "    VDIV.F64 D2, D0, D1",   
                "    VCVT.S32.F64 S4, D2",  
                "    VCVT.F64.S32 D2, S4",   
                "    VMUL.F64 D2, D2, D1",   
                "    VSUB.F64 D0, D0, D2",  
                "    VPUSH {D0}\n"
            ]
            
        elif token == "^":
            l_loop = f"pow_loop_{label_cnt}"
            l_end = f"pow_end_{label_cnt}"
            label_cnt += 1
            codigo += [
                "    VPOP {D1}",
                "    VPOP {D0}",
                "    VCVT.S32.F64 S2, D1",
                "    VMOV R1, S2",
                "    MOV R2, #1",
                "    VMOV S4, R2",
                "    VCVT.F64.S32 D2, S4",
                f"{l_loop}:",
                "    CMP R1, #0",
                f"    BLE {l_end}",
                "    VMUL.F64 D2, D2, D0",
                "    SUB R1, R1, #1",
                f"    B {l_loop}",
                f"{l_end}:",
                "    VMOV.F64 D0, D2",
                "    VPUSH {D0}\n"
            ]
            
        elif token == "RES":
            codigo += [
                "    VPOP {D1}",
                "    VCVT.S32.F64 S2, D1",
                "    VMOV R1, S2",
                "    LSL R1, R1, #3",
                "    SUB R2, R10, R1",
                "    VLDR D0, [R2]",
                "    VPUSH {D0}\n"
            ]
            
        elif token in variaveis:
            if i > 0 and tokens[i-1] == "(":
                codigo += [
                    f"    LDR R0, ={token}",
                    "    VLDR D0, [R0]",
                    "    VPUSH {D0}\n"
                ]
            else:
                codigo += [
                    "    VPOP {D0}",
                    f"    LDR R0, ={token}",
                    "    VSTR.F64 D0, [R0]\n",
                    "    VPUSH {D0}\n"
                ]
                
        else:
            l_val = f"val_{label_cnt}"
            l_skip = f"skip_{label_cnt}"
            label_cnt += 1
            codigo += [
                f"    VLDR D0, {l_val}",
                "    VPUSH {D0}",
                f"    B {l_skip}",
                "    .align 3",
                f"{l_val}: .double {token}",
                f"{l_skip}:\n"
            ]
            
    codigo += [
        "end:",
        "    B end\n"
    ]
    
    return "\n".join(codigo)