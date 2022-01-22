#!/usr/local/bin/perl5.22
print "Content-type: text/html\n\n";
 
$title='Sendmail Test';
$to='hostmysite@gmail.com';
$from= 'root@surflocal.net';
$subject='Sendmail Test';
 
open(MAIL, "|/usr/sbin/sendmail -t");
 
## Mail Header
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
## Mail Body
print MAIL "This is a test message from Cyberciti.biz! You can write your
mail body text here\n";
 
close(MAIL);
 
print "<html><head><title>$title</title></head>\n<body>\n\n";
 
## HTML content sent, let use know we sent an email
print "
<h1>$title</h1>
 
A message has been sent from $from to $to
 
</body></html>";

