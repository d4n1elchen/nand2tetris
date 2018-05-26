// push constant 17
    @17
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 17
    @17
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// eq
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_0
    D;JEQ
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_0_END
    0;JMP
(ARITHM_JMP_0)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_0_END)
// push constant 17
    @17
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 16
    @16
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// eq
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_1
    D;JEQ
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_1_END
    0;JMP
(ARITHM_JMP_1)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_1_END)
// push constant 16
    @16
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 17
    @17
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// eq
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_2
    D;JEQ
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_2_END
    0;JMP
(ARITHM_JMP_2)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_2_END)
// push constant 892
    @892
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 891
    @891
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// lt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_3
    D;JLT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_3_END
    0;JMP
(ARITHM_JMP_3)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_3_END)
// push constant 891
    @891
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 892
    @892
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// lt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_4
    D;JLT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_4_END
    0;JMP
(ARITHM_JMP_4)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_4_END)
// push constant 891
    @891
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 891
    @891
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// lt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_5
    D;JLT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_5_END
    0;JMP
(ARITHM_JMP_5)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_5_END)
// push constant 32767
    @32767
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 32766
    @32766
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// gt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_6
    D;JGT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_6_END
    0;JMP
(ARITHM_JMP_6)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_6_END)
// push constant 32766
    @32766
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 32767
    @32767
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// gt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_7
    D;JGT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_7_END
    0;JMP
(ARITHM_JMP_7)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_7_END)
// push constant 32766
    @32766
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 32766
    @32766
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// gt
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    D=M-D
    @ARITHM_JMP_8
    D;JGT
    @SP
    A=M-1
    M=0
    @ARITHM_JMP_8_END
    0;JMP
(ARITHM_JMP_8)
    @SP
    A=M-1
    M=-1
(ARITHM_JMP_8_END)
// push constant 57
    @57
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 31
    @31
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 53
    @53
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// add
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    M=D+M
// push constant 112
    @112
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// sub
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    M=M-D
// neg
    @SP
    A=M-1
    M=-M
// and
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    M=D&M
// push constant 82
    @82
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// or
    @SP
    D=M-1
    AM=D
    D=M
    A=A-1
    M=D|M
// not
    @SP
    A=M-1
    M=!M
