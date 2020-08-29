#   SMTP "MAIL FROM" message checker
#   Author: Christian Nell
#   Onyen: cnell
#   PID: 7302-29326
#   Date: 8/11/20
#   Purpose: To check a Simple Mail Transfer Protocol "MAIL FROM" message
#               and make sure it is following the correct syntax. This
#               message tells the mail server which person is trying to
#               email a message.
#
#   UNC Honor Pledge: I certify that no unauthorized assistance has been received or
#       given in the completion of this work
#       Signature: _Christian Nell__
import sys
#   Called to print out incorrect input before returning and showing ERROR -- token


def echo(string):
    counter = 0
    copy = string
    while(CRLF(string) == False):
        string = string[1:]
        counter += 1
    print(copy[0:counter])
    return False

#############################################################
##############            MAIL FROM            ##############
#############################################################


def mail_from_cmd(string):
    echo(string)
    #   checks MAIL FROM: command
    string = check_mail_from(string)
    #    <nullspace>
    string = nullspace(string)
    #   <reverse-path>
    string = reverse_path(string)
    if(not(string)):
        print("501 Syntax error in parameters or arguments")
        return False
    #    <nullspace>
    string = nullspace(string)
    if(not(string)):
        print("501 Syntax error in parameters or arguments")
        return False
    #   <CLRF>
    string = CRLF(string)
    if(string == False):
        print("501 Syntax error in parameters or arguments")
        return False
    #  Sender ok, and end of line
    if(string == True):
        return True


def check_mail_from(string):
    mailString = "MAIL"
    fromString = "FROM:"
    # MAIL
    mail = string[0:4]
    if(not(mailString == mail)):
        return False
    string = string[4:]
    #    <whitespace>
    if(SP(string) == False):
        return False
    string = whitespace(string)
    #   "FROM:"
    if(not(fromString == string[0:5])):
        return False
    string = string[5:]
    return string


def whitespace(string):
    #   <SP> | <SP> <whitespace>
    if(SP(string) == False):
        return string[0:]
    string = SP(string)
    return whitespace(string)


def SP(string):
    #   the space or tab char
    if(string[0] == ' ' or string[0] == '\t'):
        return string[1:]
    elif(string[0] == '\\'):
        if(string[1] == 't'):
            return string[2:]
    return False


def nullspace(string):
    #   <null> | <whitespace>
    if(null(string[0])):
        return string
    return whitespace(string)


def null(c):
    #  no character
    if((c != ' ') or (c != '\t')):
        return False
    return True


def reverse_path(string):
    #  <path>
    return path(string)


def path(string):
    # "<"
    if(string[0] != '<'):
        return False
    #  <mailbox>
    string = mailbox(string[1:])
    if(string == False):
        return False
    #  ">"
    if(string[0] != '>'):
        return False
    return string[1:]


def mailbox(string):
    #  <local-part>
    copy = string
    string = local_part(string)
    if(string == False or (copy[0] == string[0])):
        return False
    #  "@"
    if(string[0] != '@'):
        return False
    #  <domain>
    string = domain(string[1:])
    if(string == False):
        return False
    return string


def local_part(string):
    #   <string>
    string = string_(string)
    return string


def string_(string):
    #   <char> | <char> <string>
    if(char(string) == False):
        return string
    return string_(string[1:])


def char(string):
    #   any one of the printable ASCII characters, but not any
    #       of <special> or <SP>
    if(special(string[0]) or SP(string) or not(ord(string[0]) < 128) or CRLF(string[0])):
        return False
    return True


def domain(string):
    #   <element> | <element> "." <domain>
    string = element(string)
    if(string == False):
        return False
    if(string[0] == '.'):
        string = domain(string[1:])
    return string


def element(string):
    #  <letter> | <name>
    if(not(letter(string[0]))):
        return False
    if(name(string) != False):
        string = name(string)
    elif():
        string = string[1:]
    return string


def name(string):
    #   <letter> <let-dig-str>
    if(not(letter(string[0]))):
        return False
    return let_dig_str(string)


def letter(c):
    #   any one of the 52 alphabetic characters A through Z
    #       in upper case and a through z in lower case
    if c.isalpha():
        return True
    return False


def let_dig_str(string):
    #   <let-dig> | <let-dig> <let-dig-str>
    if(not(let_dig(string[0]))):
        return string
    return let_dig_str(string[1:])


def let_dig(c):
    #  <letter> | <digit>
    if(letter(c) or digit(c)):
        return True
    return False


def digit(c):
    #    any one of the ten digits 0 through 9
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if c in digits:
        return True
    return False


def CRLF(string):
    #    the newline character
    if(string[0] == '\n'):
        string = string[1:]
        if(len(string) == 0):
            return True
        return string[1:]
    if(string[0] == '\\'):
        if(string[1] == 'n'):
            return string[2:]
    return False


def special(c):
    #   special list ... shouldn't be in input
    special_list = ['<', '>', '(', ')', '[', ']',
                    '\\', '.', ',', ';', ':', '@', '"']
    if c in special_list:
        return True
    return False


#############################################################
##############            RCPT TO              ##############
#############################################################

def rcpt_to(string):
    echo(string)
    #   checks RCPT TO: command
    string = check_rcpt_to(string)
    #   <nullspace>
    string = nullspace(string)
    #   <forward-path>
    string = forward_path(string)
    if(not(string)):
        return False
    #   <nullspace>
    string = nullspace(string)
    #   <CRLF>
    string = CRLF(string)
    if(not(string)):
        return False
    return True


def forward_path(string):
    return path(string)


def check_rcpt_to(string):
    rcptString = "RCPT"
    toString = "TO:"
    #   "RCPT"
    if(not(rcptString == string[0:4])):
        return False
    string = string[4:]
    #    <whitespace>
    if(SP(string) == False):
        return False
    string = whitespace(string)
    #   "TO:"
    if(not(toString == string[0:3])):
        return False
    string = string[3:]
    return string

#############################################################
##############              DATA               ##############
#############################################################


def data(string):
    return null


def check_data(string):
    return False


def call_command(string, count):
    if(check_mail_from(string) != False):
        if(count != 0):
            return error503(string)
        if(mail_from_cmd(string)):
            return ok250(count)
        return error501(string)
    elif(check_rcpt_to(string) != False):
        if(count < 1):
            return error503(string)
        if(rcpt_to(string)):
            return ok250(count)
        return error501(string)
    elif(check_data(string) != False):
        if(count < 2):
            return error503(string)
        if(data(string)):
            return ok250(count)
        return error501(string)
    else:
        return error500(string)
    return True

#   500 Syntax error


def error500(string):
    echo(string)
    print("500 Syntax error: command unrecognized")
    return False

#   501 Syntax error


def error501(string):
    print("501 Syntax error in parameters or arguments")
    return False

#   503 Bad sequence


def error503(string):
    echo(string)
    print("503 Bad sequence of commands")
    return False


def ok250(count):
    print("250 OK")
    count += 1
    return count


def main():
    count = 0
    #  Get line of input from terminal and check in mail_from_cmd
    for line in sys.stdin:
        count = call_command(line, count)
        if(not(count)):
            count = 0


main()