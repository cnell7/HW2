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
        return exit()

#   Purpose:
#   Input: Counter position code is at, and the string it
#               is checking
#   Output: Will return the string position, i, that


def exit():
    return False


def mail_from_cmd(string):
    mailString = "MAIL"
    fromString = "FROM:"
    #   "MAIL"
    if(not(mailString == string[0:4])):
        print("ERROR -- mail-from-cmd")
        return exit()
    i = 4
    #    <whitespace>
    if(not(whitespace(i, string))):
        return exit()
    i = whitespace(i, string)
    #   "FROM:"
    if(not(fromString == string[i:i+5])):
        print("ERROR -- mail-from-cmd")
        return exit()
    i += 5
    #    <nullspace>
    i = nullspace(i, string)
    if (nullspace(i, string) == False):
        return exit()
    #   <reverse-path>
    if (reverse_path(i, string) == False):
        return exit()
    #    <nullspace>
    i = nullspace(i, string)
    #   <CLRF>
    CRLF(i, string)
    print("Sender ok")
    return True


def whitespace(i, string):
    if(SP(i, string) == False):
        print("ERROR -- whitespace")
        return False
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
    if(null(i, string) == True):
        return False
    if(not(SP(i, string))):
        return i
    i = whitespace(i, string)
    return i

    # NEEDS WORK


def null(i, string):
    if (length_check(i, string) == False):
        return True
    return False


def reverse_path(i, string):
    return path(i, string)


def path(i, string):
    #   "<"
    if string[i] != "<":
        print("ERROR -- path")
        return exit()

    i += 1

    #   Incomplete input check
    length_check(i, string)

    #    <mailbox>
    if (mailbox(i, string) == False):
        return False
    return i


def mailbox(i, string):
    if (local_part(i, string) == False):
        return False
    i = 1 + local_part(i, string)

    if (domain(i, string) == False):
        return False
    return i


def local_part(i, string):
    local_part_start = i

    while string[i] != "@":
        if (string_(i, string)):
            print("ERROR -- local-part")
            return exit()
        if i == (len(string) - 1):
            print("ERROR -- no @")
            return exit()
        i += 1

    if local_part_start == i:
        print("ERROR -- local-part")
        return exit()

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
            return exit()
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
    # mail_from = raw_input()

    pass1 = "MAIL FROM:<he@h"
    pass2 = "MAIL  FROM:<eh@h"
    pass3 = "MAIL  FROM: <he@h"
    pass4 = "MAIL        FROM:       <heh@h"

    fail1 = "mAIL FROM:<he@h"
    fail2 = "MAIL fROM:<he@h"
    fail3 = "MAIL FROM:< he@h"
    fail4 = " MAIL FROM:<heh@h"
    fail5 = "MAIL    FROM:"
    fail6 = "MAILFROM:<"
    fail7 = "MAIL ! FROM:<hi@hi"
    fail8 = "MAIL! FROM:<hi@hi"

    print("pass")
    print("1")
    mail_from_cmd(pass1)
    print("2")
    mail_from_cmd(pass2)
    print("3")
    mail_from_cmd(pass3)
    print("4")
    mail_from_cmd(pass4)

    print("\nfail")
    print("1 = mail from")
    mail_from_cmd(fail1)
    print("2 = mail from")
    mail_from_cmd(fail2)
    print("3 = local part")
    mail_from_cmd(fail3)
    print("4 = mail from")
    mail_from_cmd(fail4)
    print("5 = incomplete")
    mail_from_cmd(fail5)
    print("6 = whitespace")
    mail_from_cmd(fail6)
    print("7 = mail from")
    mail_from_cmd(fail7)
    print("8 = whitespace")
    mail_from_cmd(fail8)


main()
