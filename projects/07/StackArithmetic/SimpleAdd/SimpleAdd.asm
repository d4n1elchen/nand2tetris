// push constant 7
    @7
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 8
    @8
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
