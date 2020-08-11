mail_from = raw_input()

if(mail_from[0:4]!="MAIL"):
    print("ERROR -- mail")
    exit()

i = 5

while mail_from[i] == " ":
    i+=1

if(mail_from[i:i+5]!="FROM:"):
    print("ERROR -- from")
    exit()

i += 5

while mail_from[i] == " ":
    i+=1

if mail_from[i] != "<":
    print("ERROR -- path")
    exit()

i+=1
local_part = mail_from[i]

while mail_from[i] != "@":
    #need to input special character checker
    i+=1
    if i == len(mail_from):
        print("ERROR -- @")

print("Sender ok")