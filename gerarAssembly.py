def gerarAssembly(tokens):
    codigo = []

    codigo.append(".data")
    codigo.append("MEM: .float 0.0")
    codigo.append("RES: .float 0.0\n")

    codigo.append(".text")
    codigo.append(".global _start")
    codigo.append("_start:\n")

    for token in tokens:

        if token == "+":
            codigo += [
                "    VPOP {S1}",
                "    VPOP {S0}",
                "    VADD.F32 S0, S0, S1",
                "    VPUSH {S0}\n"
            ]

        elif token == "-":
            codigo += [
                "    VPOP {S1}",
                "    VPOP {S0}",
                "    VSUB.F32 S0, S0, S1",
                "    VPUSH {S0}\n"
            ]

        elif token == "*":
            codigo += [
                "    VPOP {S1}",
                "    VPOP {S0}",
                "    VMUL.F32 S0, S0, S1",
                "    VPUSH {S0}\n"
            ]

        elif token == "/":
            codigo += [
                "    VPOP {S1}",
                "    VPOP {S0}",
                "    VDIV.F32 S0, S0, S1",
                "    VPUSH {S0}\n"
            ]

       
        elif token == "^":
            codigo += [
                "    VPOP {S1}",      # expoente
                "    VPOP {S0}",      # base
                "    VMOV R1, S1",
                "    VMOV R0, S0",
                "    MOV R2, #1",     # resultado
                "pow_loop:",
                "    CMP R1, #0",
                "    BEQ pow_end",
                "    MUL R2, R2, R0",
                "    SUB R1, R1, #1",
                "    B pow_loop",
                "pow_end:",
                "    VMOV S0, R2",
                "    VPUSH {S0}\n"
            ]

        
        elif token == "%":
            codigo += [
                "    VPOP {S1}",   # b
                "    VPOP {S0}",   # a
                "    VMOV R0, S0",
                "    VMOV R1, S1",
                "    UDIV R2, R0, R1",
                "    MUL R3, R2, R1",
                "    SUB R4, R0, R3",
                "    VMOV S0, R4",
                "    VPUSH {S0}\n"
            ]

        elif token == "MEM":
            codigo += [
                "    LDR R0, =MEM",
                "    VLDR S0, [R0]",
                "    VPUSH {S0}\n"
            ]

        elif token == "RES":
            codigo += [
                "    LDR R0, =RES",
                "    VLDR S0, [R0]",
                "    VPUSH {S0}\n"
            ]

        elif token in ["(", ")"]:
            continue

        else:
            codigo += [
                f"    LDR R0, ={token}",
                "    VLDR S0, [R0]",
                "    VPUSH {S0}\n"
            ]

    codigo += [
        "    VPOP {S0}",
        "    LDR R0, =RES",
        "    VSTR S0, [R0]\n",
        "end:",
        "    B end"
    ]

    return "\n".join(codigo)