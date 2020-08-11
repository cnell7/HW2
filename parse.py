#   SMTP "MAIL FROM" message checker
#   Author: Christian Nell
#   PID: 7302-29326
#   Date: 8/11/20
#   Purpose: To check a Simple Mail Transfer Protocol "MAIL FROM" message
#               and make sure it is following the correct syntax. This
#               message tells the mail server which person is trying to
#               email a message.

#   Checks to make sure the string is not incomplete at the spot it is working on
def length_check(i, string):
    if i > (len(mail_from) - 1):
        print("ERROR -- incomplete input")
        exit()


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
while mail_from[i] == " ":
    i += 1
    length_check(i, mail_from)

#   "FROM:"
if(mail_from[i:i+5] != "FROM:"):
    print("ERROR -- from")
    exit()

i += 5

#   Incomplete input check
length_check(i, mail_from)

#   <path>
if mail_from[i] != "<":
    print("ERROR -- path")
    exit()

i += 1
#   Incomplete input check
length_check(i, mail_from)
local_part_start = i

while mail_from[i] != "@":
    if mail_from[i] == ("<" or ">" or "(" or ")" or "[" or "]" or "\'" or "." or "," or ";" or ":" or "@" or '"'):
        print("ERROR -- local-part")
        exit()
    # need to input special character checker
    if i == (len(mail_from) - 1):
        print("ERROR -- no @")
        exit()
    i += 1

if local_part_start == i:
    print("ERROR -- local-part")
    exit()

print("Sender ok")
