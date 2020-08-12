#   SMTP "MAIL FROM" message checker
#   Author: Christian Nell
#   PID: 7302-29326
#   Date: 8/11/20
#   Purpose: To check a Simple Mail Transfer Protocol "MAIL FROM" message
#               and make sure it is following the correct syntax. This
#               message tells the mail server which person is trying to
#               email a message.

#   Purpose: Checks to make sure the string is not incomplete at the spot it is working on
#   Input: Counter position code is at, and the string it
#               is checking
#   Output: None, will close program if the string is over
#               and therefore incomplete before end of the
#               SSMTP check
def length_check(i, string):
    if i > (len(string) - 1):
        print("ERROR -- incomplete input")
        exit()

    #   Purpose:
    #   Input: Counter position code is at, and the string it
    #               is checking
    #   Output: Will return the string position, i, that


def mail_from_cmd(string):
    mailString = "MAIL"
    fromString = "FROM:"

    #   "MAIL"
    if(not(mailString == string[0:4])):
        print("ERROR -- mail-from-cmd")
        exit()

    i = 5
    #    <whitespace>
    i = whitespace(i, string)

    #   "FROM:"
    if(not(fromString == string[i:i+5])):
        print("ERROR -- mail-from-cmd")
        exit()

    i += 5
    #    <nullspace>
    i = nullspace(i, string)

    #   <reverse-path>
    i = reverse_path(i, string)

    #    <nullspace>
    i = nullspace(i, string)

    #   <CLRF>
    CRLF(i, string)

    print("Sender ok")


def whitespace(i, string):
    while SP(i, string):
        i += 1
        length_check(i, string)
    return i


def SP(i, string):
    if ((" " == string[i]) or ("  " == string[i])):
        return True
    else:
        return False


def nullspace(i, string):
    i = whitespace(i, string)
    return i

    # NEEDS WORK


def null(i, string):
    return null


def reverse_path(i, string):
    return path(i, string)


def path(i, string):
    #   "<"
    if string[i] != "<":
        print("ERROR -- path")
        exit()

    i += 1

    #   Incomplete input check
    length_check(i, string)

    #    <mailbox>
    mailbox(i, string)
    return i


def mailbox(i, string):
    local_part(i, string)

    i += 3

    domain(i, string)

    return i


def local_part(i, string):
    local_part_start = i

    while string[i] != "@":
        if (string_(i, string)):
            print("ERROR -- local-part")
            exit()
        if i == (len(string) - 1):
            print("ERROR -- no @")
            exit()
        i += 1

    if local_part_start == i:
        print("ERROR -- local-part")
        exit()

    local_part = string[local_part_start:i]
    return i


def string_(i, string):
    if(special(i, string) or SP(i, string)):
        return True
    else:
        return False


def char(i, string):
    return null


def domain(i, string):
    domain_start = i

    while i != (len(string)):
        if special(i, string):
            print("ERROR -- domain")
            exit()
        i += 1

    domain = string[domain_start:i]
    return i


def element():
    return null


def name():
    return null


def letter():
    return null


def let_dig_str():
    return null


def let_dig():
    return null


def digit():
    return null


def CRLF(i, string):
    return null


def special(i, string):
    special_list = ["<", ">", "(", ")", "[", "]",
                    "\'", ".", ",", ";", ":", "@", '"']
    if string[i] in special_list:
        return True
    else:
        return False


def main():
    # Get user input from keyboard
    #mail_from = raw_input()

    pass1 = "MAIL FROM:<he@h"
    pass2 = "MAIL  FROM:<eh@h"
    pass3 = "MAIL  FROM: <he@h"
    fail1 = "mAIL FROM:<he@h"
    fail2 = "MAIL fROM:<he@h"
    fail3 = "MAIL FROM:< he@h"

    print("pass")
    mail_from_cmd(pass1)
    mail_from_cmd(pass2)
    mail_from_cmd(pass3)

    print("fail")


main()
