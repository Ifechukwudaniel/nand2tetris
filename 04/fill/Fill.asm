// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

@KBD
D=M
@23
D;JNE // if key pressed, go below and fill screen
@6
D;JEQ // else, clear the screen

@i
M=0
@i
D=M
@8192
D=A-D 
@0
D;JEQ
@i
D=M
@SCREEN
A=D+A
M=0 //fill screen
@i 
M=M+1
@8
0;JMP

@i
M=0
@i
D=M
@8192
D=A-D 
@0
D;JEQ
@i
D=M
@SCREEN
A=D+A
M=-1 //fill screen
@i 
M=M+1
@25
0;JMP

