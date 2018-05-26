// push constant 111
    @111
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 333
    @333
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// push constant 888
    @888
    D=A
    @SP
    AM=M+1
    A=A-1
    M=D
// pop static 8
    @SP
    AM=M-1
    D=M
    @f.8
    M=D
// pop static 3
    @SP
    AM=M-1
    D=M
    @f.3
    M=D
// pop static 1
    @SP
    AM=M-1
    D=M
    @f.1
    M=D
// push static 3
    @f.3
    D=M
    @SP
    AM=M+1
    A=A-1
    M=D
// push static 1
    @f.1
    D=M
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
// push static 8
    @f.8
    D=M
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
