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
    if i > (len(mail_from) - 1):
        print("ERROR -- incomplete input")
        exit()

#   Purpose:
#   Input: Counter position code is at, and the string it
#               is checking
#   Output: Will return the string position, i, that


def skip_whitespace(i, string):
    while mail_from[i] == " ":
        i += 1
        length_check(i, mail_from)
    return i


def special_check(i, string):
    if string[i] == ("<" or ">" or "(" or ")" or "[" or "]" or "\'" or "." or "," or ";" or ":" or "@" or '"'):
        return True
    else:
        return False


# Get user input from keyboard
mail_from = raw_input()

#   "MAIL"
if(mail_from[0:4] != "MAIL"):
    print("ERROR -- mail")
    exit()

i = 5

#   Incomplete input check
length_check(i, mail_from)

#    <whitespace>
i = skip_whitespace(i, mail_from)

#   "FROM:"
if(mail_from[i:i+5] != "FROM:"):
    print("ERROR -- from")
    exit()

i += 5

#   Incomplete input check
length_check(i, mail_from)

#    <whitespace>
i = skip_whitespace(i, mail_from)

#   <path>
if mail_from[i] != "<":
    print("ERROR -- path")
    exit()

i += 1

#   Incomplete input check
length_check(i, mail_from)

#    <whitespace>
i = skip_whitespace(i, mail_from)

local_part_start = i

while mail_from[i] != "@":
    if special_check(i, mail_from):
        print("ERROR -- local-part")
        exit()
    if i == (len(mail_from) - 1):
        print("ERROR -- no @")
        exit()
    i += 1

if local_part_start == i:
    print("ERROR -- local-part")
    exit()

local_part = mail_from[local_part_start:i]

i += 1

domain_start = i

while i != (len(mail_from)):
    if special_check(i, mail_from):
        print("ERROR -- domain")
        exit()
    i += 1

domain = mail_from[domain_start:i]

print("Sender ok")
