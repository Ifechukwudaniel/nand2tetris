#!/usr/local/bin/python

import sys

A_COMMAND = 0
C_COMMAND = 1
L_COMMAND = 2

def decimal_to_binary(num):
    '''
    Does backflips to convert a decimal string into a formated binary int.
    '''
    i = -1
    fnum = float(num)
    num = int(num)
    while fnum >= 0:
        fnum = fnum - 2
        i += 1

    bin_string = ''
    while i >= 0:
        new_num = num - 2**i
        if num > 0:
            bin_string += "1"
            num = new_num
        else:
            bin_string += "0"
        i -= 1

    return "%016d" % (int(bin_string),)

class Parser(object):
    def __init__(self, filename):
        self.location = -1
        self.filename = filename
        self.f = open(self.filename, 'r')

    def doStuff(self):
        commands = []
        while self.hasMoreCommands():
            self.current_command = self.advance()
            self.command_type = self.commandType()
            if  self.command_type == None:
                continue
            elif self.command_type == C_COMMAND:
                print '111' + Code().dest(self.dest()) + Code().comp(self.comp()) + Code().jump(self.jump())
            else:
                print decimal_to_binary(self.symbol())
        self.f.close()
        return commands

    def hasMoreCommands(self):
        '''
        The validation for commands happens here.
        '''
        loc = self.f.tell()
        if loc != self.location:
            self.location = loc
            return True
        else:
            return False

    def advance(self):
        return self.f.readline().strip()

    def commandType(self):
        '''
        TODO: built stricter tests here, checking for commends, empty lines,
        and improperly formatted variables.
        '''
        if not self.current_command:
            return None
        elif self.current_command.startswith('//'):
            return None
        elif self.current_command.startswith('@'):
            return A_COMMAND
        elif "=" in self.current_command or ";" in self.current_command:
            return C_COMMAND
        else:
            return L_COMMAND

    def symbol(self):
        if self.current_command.startswith('@'):
            return self.current_command[1:]
        else:
            return self.current_command

    def dest(self):
        if "=" in self.current_command:
            return self.current_command.split("=")[0]
        else:
            return None

    def comp(self):
        if "=" in self.current_command:
            return self.current_command.split("=")[1]
        else:
            return self.current_command.split(";")[0]

    def jump(self):
        if ";" in self.current_command:
            return self.current_command.split(";")[1]
        else:
            return None


class Code(object):
    def dest(self, d):
        mapping = {
            None    : "000",
            "M"     : "001",
            "D"     : "010",
            "MD"    : "011",
            "A"     : "100",
            "AM"    : "101",
            "AD"    : "110",
            "AMD"   : "111"
        }

        return mapping[d]

    def comp(self, c):
        mapping = {
        "0"     : "0101010",
        "1"     : "0111111",
        "-1"    : "0111010",
        "D"     : "0001100",
        "A"     : "0110000",
        "M"     : "1110000",
        "!D"    : "0001101",
        "!A"    : "0110001",
        "!M"    : "1110001",
        "-D"    : "0001111",
        "-A"    : "0110011",
        "-M"    : "1110011",
        "D+1"   : "0011111",
        "A+1"   : "0110111",
        "M+1"   : "1110111",
        "D-1"   : "0001110",
        "A-1"   : "0110010",
        "M-1"   : "1110010",
        "D+A"   : "0000010",
        "D+M"   : "1000010",
        "D-A"   : "0010011",
        "D-M"   : "1010011",
        "A-D"   : "0000111",
        "M-D"   : "1000111",
        "D&A"   : "0000000",
        "D&M"   : "1000000",
        "D|A"   : "0010101",
        "D|M"   : "1010101",
        }
        return mapping[c]

    def jump(self, j):
        mapping = {
            None    : "000",
            "JGT"   : "001",
            "JEQ"   : "010",
            "JGE"   : "011",
            "JLT"   : "100",
            "JNE"   : "101",
            "JLE"   : "110",
            "JMP"   : "111"
        }
        return mapping[j]


def main():
    filename = sys.argv[1]
    p = Parser(filename).doStuff()

if __name__ == "__main__":
    main()
