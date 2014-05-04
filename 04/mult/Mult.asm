// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

    @0 
    D=M
    @i 
    M=D //initialize counter: i=R0
    @2 
    M=0 //initialize result: R2=0
(LOOP)
    @i
    D=M
    @END
    D;JEQ //if i=0, return
    @1
    D=M
    @2 
    M=M+D //R2 = R2 + R1
    @i
    M=M-1 //Decrement i
    @LOOP
    0;JMP
(END)
    @END
    0;JMP
