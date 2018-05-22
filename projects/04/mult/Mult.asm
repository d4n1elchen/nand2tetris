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
// if R0 or R1 < 0:
//   R0/R1 = -R0/R1
//   sign = 1
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

// Initialize variables
    @sum
    M=0   // sum = 0
    @i
    M=0   // i = 0
    @sign
    M=0   // sign = 0

// Check if R0 or R1 is negative or zero
(CHECK_R0)
    @R0
    D=M
    @LOOP_END
    D;JEQ // if R0 == 0, goto END

    @R0
    D=M
    @CHECK_R1
    D;JGT // if R0 > 0, goto CHECK_R1

// R0 is negative
    @R0
    M=-M // R0 = -R0
    @sign
    M=!M // sing = !sign

(CHECK_R1)
    @R1
    D=M
    @LOOP_END
    D;JEQ // if R1 == 0, goto END

    @R1
    D=M
    @COMP_NUM
    D;JGT // if R1 > 0, goto COMP_NUM

// R1 is negative
    @R1
    M=-M // R1 = -R1
    @sign
    M=!M // sign = !sign

// Compare two number
(COMP_NUM)
    @R0
    D=M
    @R1
    D=D-M
    @R1_BIGGER
    D;JLT // if R0 - R1 < 0, goto R1_BIGGER else R0_BIGGER

(R0_BIGGER)
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

    @sign
    D=M
    @END
    D;JEQ // if sign == 0, goto END

// flip sign
    @R2
    M=-M

(END)
    @END
    0;JMP
