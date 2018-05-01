// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Psuedo code:
// sum = 0
// i = 0
//
// if R0 or R1 is 0:
//   goto END
//
// if R0 > R1:
//   a = R0
//   n = R1
// else:
//   a = R1
//   n = R0
// 
// if i < n:
//   sum += a
//   i++
//
// (END)
// R2 = sum

// Compare two number
    @sum
    M=0   // sum = 0
    @i
    M=0   // i = 0

    @R0
    D=M
    @LOOP_END
    D;JEQ // if R0 == 0, goto END

    @R1
    D=M
    @LOOP_END
    D;JEQ // if R1 == 0, goto END

    @R0
    D=M
    @R1
    D=D-M
    @R1_BIGGER
    D;JLT // if R0 - R1 < 0, goto R1_BIGGER

    @R0
    D=M
    @a
    M=D   // a = R0
    @R1
    D=M
    @n
    M=D   // n = R1
    @LOOP
    0;JMP // goto LOOP

(R1_BIGGER)
    @R1
    D=M
    @a
    M=D   // a = R1
    @R0
    D=M
    @n
    M=D   // n = R0

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @LOOP_END
    D;JEQ // if i - n == 0, goto LOOP_END

    @a
    D=M
    @sum
    M=M+D // sum = sum + a
    @i
    M=M+1 // i = i + 1
    @LOOP
    0;JMP

(LOOP_END)
    @sum
    D=M
    @R2
    M=D   // R2 = sum

(END)
    @END
    0;JMP
