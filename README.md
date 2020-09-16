This program extends HW1. Its purpose is to parse more SMTP commands. In addition to the “MAIL FROM” command, my parser will now recognize the “RCPT TO” and “DATA” commands. My parser is the basic engine of an SMTP server by
having it process the DATA command to receive and store the contents of a mail message in a file.

This part of the SMTP server is finished and fully functional.

-----Grammar-----

<rcpt-to-cmd_> ::= “RCPT” <whitespace_> “TO:” <nullspace_> <forward-path_> <nullspace_> <CRLF_>


<forward-path_> ::= <path_>


250 OK


<data-cmd_> ::= “DATA” <nullspace_> <CRLF_>
354 Start mail input; end with <CRLF_>.<CRLF_>


500 Syntax error: command unrecognized


501 Syntax error in parameters or arguments


503 Bad sequence of commands


(Some of the grammar tokens are not the same as the comments in the code. This is because github is hiding the token names inside the <>. That is also why there are extra '_'.)
