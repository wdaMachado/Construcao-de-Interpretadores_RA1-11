.data
RES_ARRAY: .space 8000
MEM: .double 0.0
.text
.global _start
_start:

    LDR R10, =RES_ARRAY

    VLDR D0, val_0
    VPUSH {D0}
    B skip_0
    .align 3
val_0: .double 10.0
skip_0:

    VPOP {D0}
    LDR R0, =MEM
    VSTR.F64 D0, [R0]

    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    LDR R0, =MEM
    VLDR D0, [R0]
    VPUSH {D0}

    VLDR D0, val_1
    VPUSH {D0}
    B skip_1
    .align 3
val_1: .double 2.0
skip_1:

    VPOP {D1}
    VPOP {D0}
    VMUL.F64 D0, D0, D1
    VPUSH {D0}

    VLDR D0, val_2
    VPUSH {D0}
    B skip_2
    .align 3
val_2: .double 5.0
skip_2:

    VPOP {D1}
    VPOP {D0}
    VADD.F64 D0, D0, D1
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    LDR R0, =MEM
    VLDR D0, [R0]
    VPUSH {D0}

    VLDR D0, val_3
    VPUSH {D0}
    B skip_3
    .align 3
val_3: .double 3.0
skip_3:

    VPOP {D1}
    VPOP {D0}
    VDIV.F64 D0, D0, D1
    VCVT.S32.F64 S0, D0
    VCVT.F64.S32 D0, S0
    VPUSH {D0}

    VLDR D0, val_4
    VPUSH {D0}
    B skip_4
    .align 3
val_4: .double 2.0
skip_4:

    VPOP {D1}
    VPOP {D0}
    VDIV.F64 D2, D0, D1
    VCVT.S32.F64 S4, D2
    VCVT.F64.S32 D2, S4
    VMUL.F64 D2, D2, D1
    VSUB.F64 D0, D0, D2
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_5
    VPUSH {D0}
    B skip_5
    .align 3
val_5: .double 2.0
skip_5:

    VLDR D0, val_6
    VPUSH {D0}
    B skip_6
    .align 3
val_6: .double 4.0
skip_6:

    VPOP {D1}
    VPOP {D0}
    VCVT.S32.F64 S2, D1
    VMOV R1, S2
    MOV R2, #1
    VMOV S4, R2
    VCVT.F64.S32 D2, S4
pow_loop_7:
    CMP R1, #0
    BLE pow_end_7
    VMUL.F64 D2, D2, D0
    SUB R1, R1, #1
    B pow_loop_7
pow_end_7:
    VMOV.F64 D0, D2
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_8
    VPUSH {D0}
    B skip_8
    .align 3
val_8: .double 1
skip_8:

    VPOP {D1}
    VCVT.S32.F64 S2, D1
    VMOV R1, S2
    LSL R1, R1, #3
    SUB R2, R10, R1
    VLDR D0, [R2]
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_9
    VPUSH {D0}
    B skip_9
    .align 3
val_9: .double 5.0
skip_9:

    VLDR D0, val_10
    VPUSH {D0}
    B skip_10
    .align 3
val_10: .double 2.0
skip_10:

    VPOP {D1}
    VPOP {D0}
    VMUL.F64 D0, D0, D1
    VPUSH {D0}

    VLDR D0, val_11
    VPUSH {D0}
    B skip_11
    .align 3
val_11: .double 3.0
skip_11:

    VPOP {D1}
    VPOP {D0}
    VSUB.F64 D0, D0, D1
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_12
    VPUSH {D0}
    B skip_12
    .align 3
val_12: .double 20.0
skip_12:

    VLDR D0, val_13
    VPUSH {D0}
    B skip_13
    .align 3
val_13: .double 3.0
skip_13:

    VPOP {D1}
    VPOP {D0}
    VDIV.F64 D2, D0, D1
    VCVT.S32.F64 S4, D2
    VCVT.F64.S32 D2, S4
    VMUL.F64 D2, D2, D1
    VSUB.F64 D0, D0, D2
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_14
    VPUSH {D0}
    B skip_14
    .align 3
val_14: .double 10.0
skip_14:

    VLDR D0, val_15
    VPUSH {D0}
    B skip_15
    .align 3
val_15: .double 2.0
skip_15:

    VPOP {D1}
    VPOP {D0}
    VSUB.F64 D0, D0, D1
    VPUSH {D0}

    VLDR D0, val_16
    VPUSH {D0}
    B skip_16
    .align 3
val_16: .double 2.0
skip_16:

    VPOP {D1}
    VPOP {D0}
    VCVT.S32.F64 S2, D1
    VMOV R1, S2
    MOV R2, #1
    VMOV S4, R2
    VCVT.F64.S32 D2, S4
pow_loop_17:
    CMP R1, #0
    BLE pow_end_17
    VMUL.F64 D2, D2, D0
    SUB R1, R1, #1
    B pow_loop_17
pow_end_17:
    VMOV.F64 D0, D2
    VPUSH {D0}

    VLDR D0, val_18
    VPUSH {D0}
    B skip_18
    .align 3
val_18: .double 2.0
skip_18:

    VPOP {D1}
    VPOP {D0}
    VDIV.F64 D0, D0, D1
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_19
    VPUSH {D0}
    B skip_19
    .align 3
val_19: .double 3.14
skip_19:

    VLDR D0, val_20
    VPUSH {D0}
    B skip_20
    .align 3
val_20: .double 2.0
skip_20:

    VPOP {D1}
    VPOP {D0}
    VMUL.F64 D0, D0, D1
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

    VLDR D0, val_21
    VPUSH {D0}
    B skip_21
    .align 3
val_21: .double 3
skip_21:

    VPOP {D1}
    VCVT.S32.F64 S2, D1
    VMOV R1, S2
    LSL R1, R1, #3
    SUB R2, R10, R1
    VLDR D0, [R2]
    VPUSH {D0}

    VPOP {D0}
    VSTR.F64 D0, [R10]
    ADD R10, R10, #8

end:
    B end
