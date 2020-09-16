This program extends HW1. Its purpose is to parse more SMTP commands. In addition to the “MAIL FROM” command, my parser will now recognize the “RCPT TO” and “DATA” commands. My parser is the basic engine of an SMTP server by
having it process the DATA command to receive and store the contents of a mail message in a file.

This part of the SMTP server is finished and fully functional.

-----Grammar-----

<rcpt-to-cmd> ::= “RCPT” <whitespace> “TO:” <nullspace> <forward-path>
<nullspace> <CRLF>
<forward-path> ::= <path>
250 OK
<data-cmd> ::= “DATA” <nullspace> <CRLF>
354 Start mail input; end with <CRLF>.<CRLF>


500 Syntax error: command unrecognized
501 Syntax error in parameters or arguments
503 Bad sequence of commands
